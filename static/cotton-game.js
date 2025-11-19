// Game state
let gameState = null;
let currentPlayerId = null;

// Initialize game on page load
document.addEventListener('DOMContentLoaded', () => {
    loadGameState();
});

async function loadGameState() {
    try {
        const response = await fetch('/api/game/state');
        if (response.ok) {
            gameState = await response.json();
            renderGame();
        } else {
            // No game exists, show new game option
            addEvent('info', 'No active game. Click "New Game" to start!');
        }
    } catch (error) {
        console.error('Error loading game:', error);
        addEvent('error', 'Failed to load game state');
    }
}

async function startNewGame() {
    try {
        const response = await fetch('/api/game/new', { method: 'POST' });
        if (response.ok) {
            gameState = await response.json();
            addEvent('success', 'New game started!');
            renderGame();
        } else {
            addEvent('error', 'Failed to start new game');
        }
    } catch (error) {
        console.error('Error starting game:', error);
        addEvent('error', 'Failed to start new game');
    }
}

async function nextTurn() {
    try {
        const response = await fetch('/api/game/turn', { method: 'POST' });
        if (response.ok) {
            gameState = await response.json();
            addEvent('info', `Turn ${gameState.turn} - ${gameState.season} season`);
            renderGame();
        } else {
            const error = await response.json();
            addEvent('error', error.error || 'Failed to advance turn');
        }
    } catch (error) {
        console.error('Error advancing turn:', error);
        addEvent('error', 'Failed to advance turn');
    }
}

function renderGame() {
    if (!gameState) return;

    // Update header info
    document.getElementById('currentSeason').innerHTML = 
        `${gameState.season} <span class="season-indicator season-${gameState.season.toLowerCase()}">Turn ${gameState.turn}</span>`;
    document.getElementById('spotPrice').textContent = `$${gameState.spotPrice.toFixed(2)}`;
    document.getElementById('futuresPrice').textContent = `$${gameState.futuresPrice.toFixed(2)}`;

    // Render players
    renderPlayers();
    
    // Render futures market
    renderFuturesMarket();
}

function renderPlayers() {
    const container = document.getElementById('playersSection');
    container.innerHTML = '';

    gameState.players.forEach(player => {
        const card = document.createElement('div');
        card.className = `player-card ${player.role}`;
        
        const roleClass = `badge-${player.role}`;
        const roleName = player.role.charAt(0).toUpperCase() + player.role.slice(1);
        
        card.innerHTML = `
            <h3>
                ${player.name}
                <span class="role-badge ${roleClass}">${roleName}</span>
            </h3>
            <div class="player-stats">
                <div class="stat-row">
                    <span class="stat-label">Cash:</span>
                    <span class="stat-value ${player.cash >= 0 ? 'positive' : 'negative'}">$${player.cash.toFixed(2)}</span>
                </div>
                <div class="stat-row">
                    <span class="stat-label">Cotton (lbs):</span>
                    <span class="stat-value">${player.cotton.toLocaleString()}</span>
                </div>
                <div class="stat-row">
                    <span class="stat-label">Futures Contracts:</span>
                    <span class="stat-value">${player.futuresContracts.length}</span>
                </div>
                <div class="stat-row">
                    <span class="stat-label">Net Worth:</span>
                    <span class="stat-value ${player.netWorth >= 0 ? 'positive' : 'negative'}">$${player.netWorth.toFixed(2)}</span>
                </div>
            </div>
            <div class="actions">
                <button onclick="selectPlayer(${player.id})">Play as ${player.name}</button>
                ${currentPlayerId === player.id ? '<span style="color: green;">✓ Active</span>' : ''}
            </div>
        `;
        
        container.appendChild(card);
    });
}

function renderFuturesMarket() {
    const tbody = document.getElementById('futuresTableBody');
    tbody.innerHTML = '';

    if (!gameState.futuresContracts || gameState.futuresContracts.length === 0) {
        tbody.innerHTML = '<tr><td colspan="5" style="text-align: center; color: #999;">No futures contracts available yet</td></tr>';
        return;
    }

    gameState.futuresContracts.forEach(contract => {
        const row = document.createElement('tr');
        
        // Find player's position in this contract
        const currentPlayer = gameState.players.find(p => p.id === currentPlayerId);
        const playerPosition = currentPlayer 
            ? currentPlayer.futuresContracts.find(fc => fc.contractId === contract.id)
            : null;
        
        const positionText = playerPosition 
            ? `${playerPosition.quantity > 0 ? 'Long' : 'Short'} ${Math.abs(playerPosition.quantity)}`
            : 'None';
        
        row.innerHTML = `
            <td>${contract.month}</td>
            <td class="${contract.priceChange >= 0 ? 'price-up' : 'price-down'}">
                $${contract.price.toFixed(2)} 
                ${contract.priceChange !== 0 ? `(${contract.priceChange >= 0 ? '+' : ''}${contract.priceChange.toFixed(2)})` : ''}
            </td>
            <td>${contract.openInterest}</td>
            <td>${positionText}</td>
            <td>
                <button onclick="openTradeModal('${contract.id}', ${contract.price})">Trade</button>
            </td>
        `;
        
        tbody.appendChild(row);
    });
}

function selectPlayer(playerId) {
    currentPlayerId = playerId;
    addEvent('info', `Now playing as ${gameState.players.find(p => p.id === playerId).name}`);
    renderGame();
}

function showMarketModal() {
    document.getElementById('tradeModal').style.display = 'block';
    populateContractMonths();
}

function closeModal() {
    document.getElementById('tradeModal').style.display = 'none';
}

function populateContractMonths() {
    const select = document.getElementById('contractMonth');
    select.innerHTML = '<option value="">Select month...</option>';
    
    if (gameState && gameState.futuresContracts) {
        gameState.futuresContracts.forEach(contract => {
            const option = document.createElement('option');
            option.value = contract.id;
            option.textContent = `${contract.month} - $${contract.price.toFixed(2)}`;
            select.appendChild(option);
        });
    }
}

function openTradeModal(contractId, currentPrice) {
    if (!currentPlayerId) {
        addEvent('warning', 'Please select a player first');
        return;
    }
    
    document.getElementById('tradeModal').style.display = 'block';
    document.getElementById('contractMonth').value = contractId;
    document.getElementById('tradePrice').value = currentPrice.toFixed(2);
    populateContractMonths();
}

async function executeTrade(event) {
    event.preventDefault();
    
    if (!currentPlayerId) {
        addEvent('warning', 'Please select a player first');
        return;
    }

    const contractId = document.getElementById('contractMonth').value;
    const action = document.getElementById('tradeAction').value;
    const quantity = parseInt(document.getElementById('tradeQuantity').value);
    const price = parseFloat(document.getElementById('tradePrice').value);

    try {
        const response = await fetch('/api/game/trade', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                playerId: currentPlayerId,
                contractId: contractId,
                action: action,
                quantity: quantity,
                price: price
            })
        });

        if (response.ok) {
            gameState = await response.json();
            addEvent('success', `Trade executed: ${action} ${quantity} contract(s) at $${price.toFixed(2)}`);
            closeModal();
            renderGame();
        } else {
            const error = await response.json();
            addEvent('error', error.error || 'Trade failed');
        }
    } catch (error) {
        console.error('Error executing trade:', error);
        addEvent('error', 'Failed to execute trade');
    }
}

function addEvent(type, message) {
    const log = document.getElementById('eventLog');
    const event = document.createElement('div');
    event.className = `event ${type}`;
    event.textContent = `[${new Date().toLocaleTimeString()}] ${message}`;
    log.insertBefore(event, log.firstChild);
    
    // Keep only last 50 events
    while (log.children.length > 50) {
        log.removeChild(log.lastChild);
    }
}

// Close modal when clicking outside
window.onclick = function(event) {
    const modal = document.getElementById('tradeModal');
    if (event.target === modal) {
        closeModal();
    }
}

