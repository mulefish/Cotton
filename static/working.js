const selectEl = document.getElementById('selecter');
const selectionSummary = document.getElementById('selectionSummary');
const tableBody = document.querySelector('#selectionTable tbody');
const fetchButton = document.getElementById('fetchBtn');
const errorMessage = document.getElementById('errorMessage');
const selectedValues = new Set();

function updateSelection() {
    selectedValues.clear();
    Array.from(selectEl.selectedOptions).forEach(option => selectedValues.add(option.value));
    renderSelectionSummary();
}

function renderSelectionSummary() {
    selectionSummary.innerHTML = '';
    if (selectedValues.size === 0) {
        const li = document.createElement('li');
        li.textContent = '(none)';
        selectionSummary.appendChild(li);
        return;
    }
    selectedValues.forEach(value => {
        const li = document.createElement('li');
        li.textContent = value;
        selectionSummary.appendChild(li);
    });
}

function renderResults(rows) {
    tableBody.innerHTML = '';
    if (!rows.length) {
        const row = document.createElement('tr');
        const cell = document.createElement('td');
        cell.colSpan = 4;
        cell.textContent = 'No data';
        row.appendChild(cell);
        tableBody.appendChild(row);
        return;
    }
    rows.forEach(({ colorGrade, leafGrade, stapleCode, count }) => {
        const row = document.createElement('tr');
        [colorGrade, leafGrade, stapleCode, count].forEach(value => {
            const cell = document.createElement('td');
            cell.textContent = value ?? '';
            row.appendChild(cell);
        });
        tableBody.appendChild(row);
    });
}

async function fetchData() {
    errorMessage.textContent = '';
    renderResults([]);

    try {
        const response = await fetch('/api/summary', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ fields: Array.from(selectedValues) }),
        });

        if (!response.ok) {
            throw new Error(`Server responded with ${response.status}`);
        }

        const payload = await response.json();
        renderResults(payload.summary || []);
    } catch (err) {
        errorMessage.textContent = `Error fetching data: ${err.message}`;
    }
}

selectEl.addEventListener('change', updateSelection);
fetchButton.addEventListener('click', fetchData);
renderSelectionSummary();