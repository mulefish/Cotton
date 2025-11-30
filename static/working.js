const selectEl = document.getElementById('selecter');
const selectionSummary = document.getElementById('selectionSummary');
const tableBody = document.querySelector('#selectionTable tbody');
const tableHeadRow = document.getElementById('selectionHeaderRow');
const fetchButton = document.getElementById('fetchBtn');
const errorMessage = document.getElementById('errorMessage');
const limitSelect = document.getElementById('limit');
const rotateToggle = document.getElementById('rotateToggle');
const highlightToggle = document.getElementById('highlightToggle');
const notesToggle = document.getElementById('notesToggle');
const notesContainer = document.getElementById('notesContainer');
const notesTextarea = document.getElementById('notes');
const showModalBtn = document.getElementById('showModalBtn');
const snippetModal = document.getElementById('snippetModal');
const closeModalBtn = document.getElementById('closeModalBtn');
const selectedValues = new Set();
let latestSummary = [];
let latestFields = [];
let sortState = { field: null, direction: 'desc' };

function updateSelection() {
    selectedValues.clear();
    Array.from(selectEl.selectedOptions).forEach(option => selectedValues.add(option.value));
    renderSelectionSummary();
}

function renderSelectionSummary() {
    if (!selectionSummary) {
        return;
    }
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

function renderTableHeader(fields) {
    tableHeadRow.innerHTML = '';
    fields.forEach(field => {
        const th = document.createElement('th');
        th.classList.add('vertical-header');
        th.appendChild(createHeaderButton(field, field));
        tableHeadRow.appendChild(th);
    });
    const countHeader = document.createElement('th');
    countHeader.classList.add('vertical-header');
    countHeader.appendChild(createHeaderButton('count', 'count'));
    tableHeadRow.appendChild(countHeader);
}

function createHeaderButton(field, label) {
    const button = document.createElement('button');
    button.type = 'button';
    button.className = 'header-button';
    button.textContent = `${label}${headerSortSuffix(field)}`;
    button.addEventListener('click', () => {
        updateSortState(field);
        rerender();
    });
    return button;
}

function headerSortSuffix(field) {
    if (sortState.field !== field) {
        return '';
    }
    return sortState.direction === 'asc' ? ' ▲' : ' ▼';
}

function renderResults(rows, fields) {
    tableBody.innerHTML = '';
    if (!rows.length) {
        const row = document.createElement('tr');
        const cell = document.createElement('td');
        cell.colSpan = fields.length + 1;
        cell.textContent = 'No data';
        row.appendChild(cell);
        tableBody.appendChild(row);
        return;
    }
    let previousRowValues = null;
    rows.forEach((rowData) => {
        const row = document.createElement('tr');
        const currentValues = [];
        fields.forEach((field, index) => {
            const cell = document.createElement('td');
            const value = rowData[field] ?? '';
            cell.textContent = value;
            currentValues[index] = value;
            if (
                highlightToggleChecked() &&
                previousRowValues &&
                previousRowValues[index] !== value
            ) {
                cell.style.backgroundColor = 'yellow';
            }
            row.appendChild(cell);
        });
        const countCell = document.createElement('td');
        const countValue = rowData.count ?? 0;
        countCell.textContent = countValue;
        row.appendChild(countCell);
        tableBody.appendChild(row);
        previousRowValues = [...currentValues, countValue];
    });
}

function currentFields() {
    return Array.from(selectedValues);
}

function currentCountThreshold() {
    if (!limitSelect) {
        return 0;
    }
    const value = Number(limitSelect.value);
    return Number.isFinite(value) ? value : 0;
}

function highlightToggleChecked() {
    return highlightToggle ? highlightToggle.checked : true;
}

function rerender() {
    if (!latestFields.length) {
        return;
    }
    const threshold = currentCountThreshold();
    const filtered = latestSummary.filter(item => (item.count ?? 0) >= threshold);
    const sorted = applySort(filtered);
    renderTableHeader(latestFields);
    renderResults(sorted, latestFields);
    updateVisualization();
}

async function fetchData() {
    errorMessage.textContent = '';
    tableHeadRow.innerHTML = '';
    tableBody.innerHTML = '';
    const loadingRow = document.createElement('tr');
    const loadingCell = document.createElement('td');
    loadingCell.textContent = 'Loading...';
    loadingRow.appendChild(loadingCell);
    tableBody.appendChild(loadingRow);

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
        const fields = Array.isArray(payload.requestedFields)
            ? payload.requestedFields.filter(Boolean)
            : [];

        if (!fields.length) {
            throw new Error('Server did not return requested fields');
        }

        latestFields = fields;
        latestSummary = payload.summary || [];
        sortState = { field: null, direction: 'desc' };
        rerender();
        updateVisualization();
    } catch (err) {
        errorMessage.textContent = `Error fetching data: ${err.message}`;
        tableHeadRow.innerHTML = '';
        tableBody.innerHTML = '';
        latestFields = [];
        latestSummary = [];
    }
}

function updateRotationSetting() {
    if (!rotateToggle) {
        return;
    }
    document.body.classList.toggle('rotate-headers', rotateToggle.checked);
}

function updateSortState(field) {
    if (sortState.field === field) {
        sortState.direction = sortState.direction === 'asc' ? 'desc' : 'asc';
    } else {
        sortState = { field, direction: 'desc' };
    }
}

function applySort(rows) {
    if (!sortState.field) {
        return rows;
    }
    const directionFactor = sortState.direction === 'asc' ? 1 : -1;
    const field = sortState.field;
    return [...rows].sort((a, b) => {
        const aValue = getComparableValue(a, field);
        const bValue = getComparableValue(b, field);
        if (aValue < bValue) {
            return -1 * directionFactor;
        }
        if (aValue > bValue) {
            return 1 * directionFactor;
        }
        return 0;
    });
}

function getComparableValue(row, field) {
    if (field === 'count') {
        const value = Number(row.count);
        return Number.isFinite(value) ? value : -Infinity;
    }
    const value = row[field];
    if (value === undefined || value === null) {
        return '';
    }
    return String(value).toLowerCase();
}

selectEl.addEventListener('change', updateSelection);
fetchButton.addEventListener('click', fetchData);
if (limitSelect && !limitSelect.hasAttribute('onchange')) {
    limitSelect.addEventListener('change', rerender);
}
if (rotateToggle) {
    rotateToggle.addEventListener('change', () => {
        updateRotationSetting();
        if (latestFields.length) {
            rerender();
        }
    });
    updateRotationSetting();
}
if (highlightToggle) {
    highlightToggle.addEventListener('change', rerender);
}
if (notesToggle && notesContainer) {
    notesToggle.addEventListener('change', () => {
        notesContainer.style.display = notesToggle.checked ? 'block' : 'none';
    });
    notesContainer.style.display = 'none';
    notesToggle.checked = false;
}
if (showModalBtn && snippetModal) {
    showModalBtn.addEventListener('click', () => {
        snippetModal.style.display = 'flex';
    });
}
if (closeModalBtn && snippetModal) {
    closeModalBtn.addEventListener('click', () => {
        snippetModal.style.display = 'none';
    });
    snippetModal.addEventListener('click', (event) => {
        if (event.target === snippetModal) {
            snippetModal.style.display = 'none';
        }
    });
}

// Initialize with pre-selected fields (colorGrade, leafGrade, stapleCode)
updateSelection();
renderSelectionSummary();

function saveNotes1() {
    persistNotes('save1');
}

function saveNotes2() {
    persistNotes('save2');
}

function loadNotes1() {
    loadNotes('save1');
}

function loadNotes2() {
    loadNotes('save2');
}

function persistNotes(key) {
    if (!notesTextarea) {
        return;
    }
    try {
        localStorage.setItem(key, notesTextarea.value);
    } catch (err) {
        errorMessage.textContent = `Unable to save notes (${err.message})`;
    }
}

function loadNotes(key) {
    if (!notesTextarea) {
        return;
    }
    try {
        const value = localStorage.getItem(key);
        if (value !== null) {
            notesTextarea.value = value;
        } else {
            notesTextarea.value = '';
        }
    } catch (err) {
        errorMessage.textContent = `Unable to load notes (${err.message})`;
    }
}

// ============================================================================
// Visualization Functions
// ============================================================================

const vizCanvas = document.getElementById('vizCanvas');
const vizTypeSelect = document.getElementById('vizType');
const vizMessage = document.getElementById('vizMessage');
const ctx = vizCanvas ? vizCanvas.getContext('2d') : null;

const DATE_FIELDS = ['issueDate', 'classDate', 'storagePaidThrough'];

function isDateField(fieldName) {
    return DATE_FIELDS.includes(fieldName);
}

function parseDate(dateStr) {
    if (!dateStr || dateStr.length !== 8) return null;
    // Format: YYYYMMDD
    const year = parseInt(dateStr.substring(0, 4));
    const month = parseInt(dateStr.substring(4, 6)) - 1;
    const day = parseInt(dateStr.substring(6, 8));
    if (isNaN(year) || isNaN(month) || isNaN(day)) return null;
    return new Date(year, month, day);
}

function isNumeric(value) {
    return !isNaN(value) && !isNaN(parseFloat(value)) && isFinite(value);
}

function getNumericField(fields, data) {
    for (const field of fields) {
        if (field === 'count') continue;
        const sample = data.find(d => d[field] !== undefined && d[field] !== null && d[field] !== '');
        if (sample && isNumeric(sample[field])) {
            return field;
        }
    }
    return null;
}

function updateVisualization() {
    if (!ctx || !vizTypeSelect || !latestSummary.length || !latestFields.length) {
        if (vizMessage) {
            vizMessage.textContent = latestSummary.length ? 'Select a chart type to visualize' : 'Select fields and fetch data to visualize';
        }
        return;
    }

    const vizType = vizTypeSelect.value;
    if (vizType === 'none') {
        clearCanvas();
        if (vizMessage) vizMessage.textContent = 'Select a chart type to visualize';
        return;
    }

    const threshold = currentCountThreshold();
    const filtered = latestSummary.filter(item => (item.count ?? 0) >= threshold);

    if (vizType === 'timeseries') {
        renderTimeSeries(filtered);
    } else if (vizType === 'barchart') {
        renderBarChart(filtered);
    } else if (vizType === 'scatter') {
        renderScatterPlot(filtered);
    } else if (vizType === 'histogram') {
        renderHistogram(filtered);
    }
}

function clearCanvas() {
    if (ctx) {
        ctx.clearRect(0, 0, vizCanvas.width, vizCanvas.height);
    }
}

function renderTimeSeries(data) {
    clearCanvas();
    const dateField = latestFields.find(f => isDateField(f));
    
    if (!dateField) {
        if (vizMessage) vizMessage.textContent = 'Time series requires a date field (issueDate, classDate, or storagePaidThrough)';
        return;
    }

    // Group by date and sum counts
    const dateMap = new Map();
    data.forEach(item => {
        const dateStr = item[dateField];
        if (!dateStr) return;
        const date = parseDate(dateStr);
        if (!date) return;
        const key = date.toISOString().split('T')[0];
        dateMap.set(key, (dateMap.get(key) || 0) + (item.count || 0));
    });

    if (dateMap.size === 0) {
        if (vizMessage) vizMessage.textContent = 'No valid date data found';
        return;
    }

    const dates = Array.from(dateMap.keys()).sort();
    const values = dates.map(d => dateMap.get(d));
    const maxValue = Math.max(...values);
    const minValue = Math.min(...values);
    const range = maxValue - minValue || 1;

    const padding = 60;
    const width = vizCanvas.width - 2 * padding;
    const height = vizCanvas.height - 2 * padding;
    const xStep = width / (dates.length - 1 || 1);

    // Draw axes
    ctx.strokeStyle = '#333';
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(padding, padding);
    ctx.lineTo(padding, height + padding);
    ctx.lineTo(width + padding, height + padding);
    ctx.stroke();

    // Draw grid and labels
    ctx.fillStyle = '#666';
    ctx.font = '10px Arial';
    ctx.textAlign = 'right';
    ctx.textBaseline = 'middle';
    
    // Y-axis labels
    for (let i = 0; i <= 5; i++) {
        const y = height + padding - (i * height / 5);
        const value = minValue + (i * range / 5);
        ctx.fillText(Math.round(value).toLocaleString(), padding - 5, y);
        ctx.strokeStyle = '#ddd';
        ctx.beginPath();
        ctx.moveTo(padding, y);
        ctx.lineTo(width + padding, y);
        ctx.stroke();
        ctx.strokeStyle = '#333';
    }

    // X-axis labels (show first, middle, last)
    ctx.textAlign = 'center';
    ctx.textBaseline = 'top';
    if (dates.length > 0) {
        [0, Math.floor(dates.length / 2), dates.length - 1].forEach(idx => {
            if (idx < dates.length) {
                const x = padding + idx * xStep;
                const label = dates[idx].substring(5); // MM-DD
                ctx.fillText(label, x, height + padding + 5);
            }
        });
    }

    // Draw line
    ctx.strokeStyle = '#2196F3';
    ctx.lineWidth = 2;
    ctx.beginPath();
    dates.forEach((date, idx) => {
        const x = padding + idx * xStep;
        const y = height + padding - ((values[idx] - minValue) / range * height);
        if (idx === 0) {
            ctx.moveTo(x, y);
        } else {
            ctx.lineTo(x, y);
        }
    });
    ctx.stroke();

    // Draw points
    ctx.fillStyle = '#2196F3';
    dates.forEach((date, idx) => {
        const x = padding + idx * xStep;
        const y = height + padding - ((values[idx] - minValue) / range * height);
        ctx.beginPath();
        ctx.arc(x, y, 3, 0, 2 * Math.PI);
        ctx.fill();
    });

    if (vizMessage) vizMessage.textContent = `Time Series: ${dateField} (${dates.length} data points)`;
}

function renderBarChart(data) {
    clearCanvas();
    
    // Use first categorical field or count
    const catField = latestFields.find(f => f !== 'count') || 'count';
    
    // Group by category
    const categoryMap = new Map();
    data.forEach(item => {
        const key = item[catField] || 'N/A';
        categoryMap.set(key, (categoryMap.get(key) || 0) + (item.count || 0));
    });

    const categories = Array.from(categoryMap.keys()).slice(0, 20); // Limit to 20
    const values = categories.map(cat => categoryMap.get(cat));
    const maxValue = Math.max(...values, 1);

    const padding = 60;
    const width = vizCanvas.width - 2 * padding;
    const height = vizCanvas.height - 2 * padding;
    const barWidth = width / categories.length * 0.8;
    const barSpacing = width / categories.length * 0.2;

    // Draw axes
    ctx.strokeStyle = '#333';
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(padding, padding);
    ctx.lineTo(padding, height + padding);
    ctx.lineTo(width + padding, height + padding);
    ctx.stroke();

    // Draw bars
    ctx.fillStyle = '#4CAF50';
    categories.forEach((cat, idx) => {
        const x = padding + idx * (barWidth + barSpacing);
        const barHeight = (values[idx] / maxValue) * height;
        const y = height + padding - barHeight;
        
        ctx.fillRect(x, y, barWidth, barHeight);
        
        // Label
        ctx.fillStyle = '#333';
        ctx.font = '9px Arial';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'top';
        const label = String(cat).substring(0, 8);
        ctx.fillText(label, x + barWidth / 2, height + padding + 3);
        ctx.fillStyle = '#4CAF50';
    });

    // Y-axis labels
    ctx.fillStyle = '#666';
    ctx.font = '10px Arial';
    ctx.textAlign = 'right';
    ctx.textBaseline = 'middle';
    for (let i = 0; i <= 5; i++) {
        const y = height + padding - (i * height / 5);
        const value = Math.round(i * maxValue / 5);
        ctx.fillText(value.toLocaleString(), padding - 5, y);
    }

    if (vizMessage) vizMessage.textContent = `Bar Chart: ${catField} (${categories.length} categories)`;
}

function renderScatterPlot(data) {
    clearCanvas();
    
    const xField = getNumericField(latestFields, data);
    const yField = latestFields.includes('count') ? 'count' : getNumericField(latestFields.filter(f => f !== xField), data);
    
    if (!xField || !yField) {
        if (vizMessage) vizMessage.textContent = 'Scatter plot requires at least one numeric field';
        return;
    }

    const points = data
        .map(item => ({
            x: parseFloat(item[xField]) || 0,
            y: parseFloat(item[yField]) || 0,
            size: item.count || 1
        }))
        .filter(p => !isNaN(p.x) && !isNaN(p.y));

    if (points.length === 0) {
        if (vizMessage) vizMessage.textContent = 'No valid numeric data found';
        return;
    }

    const xValues = points.map(p => p.x);
    const yValues = points.map(p => p.y);
    const xMin = Math.min(...xValues);
    const xMax = Math.max(...xValues);
    const yMin = Math.min(...yValues);
    const yMax = Math.max(...yValues);
    const xRange = xMax - xMin || 1;
    const yRange = yMax - yMin || 1;

    const padding = 60;
    const width = vizCanvas.width - 2 * padding;
    const height = vizCanvas.height - 2 * padding;

    // Draw axes
    ctx.strokeStyle = '#333';
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(padding, padding);
    ctx.lineTo(padding, height + padding);
    ctx.lineTo(width + padding, height + padding);
    ctx.stroke();

    // Draw points
    ctx.fillStyle = 'rgba(33, 150, 243, 0.6)';
    points.forEach(point => {
        const x = padding + ((point.x - xMin) / xRange) * width;
        const y = height + padding - ((point.y - yMin) / yRange) * height;
        const radius = Math.min(5, 2 + Math.log(point.size || 1));
        ctx.beginPath();
        ctx.arc(x, y, radius, 0, 2 * Math.PI);
        ctx.fill();
    });

    // Labels
    ctx.fillStyle = '#666';
    ctx.font = '10px Arial';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'top';
    ctx.fillText(xField, width / 2 + padding, height + padding + 10);
    
    ctx.save();
    ctx.translate(15, height / 2 + padding);
    ctx.rotate(-Math.PI / 2);
    ctx.textAlign = 'center';
    ctx.fillText(yField, 0, 0);
    ctx.restore();

    if (vizMessage) vizMessage.textContent = `Scatter Plot: ${xField} vs ${yField} (${points.length} points)`;
}

function renderHistogram(data) {
    clearCanvas();
    
    const numField = getNumericField(latestFields, data) || 'count';
    
    const values = data
        .flatMap(item => {
            const val = parseFloat(item[numField]);
            const count = item.count || 1;
            return isNaN(val) ? [] : Array(count).fill(val);
        })
        .filter(v => !isNaN(v));

    if (values.length === 0) {
        if (vizMessage) vizMessage.textContent = 'No valid numeric data found';
        return;
    }

    const min = Math.min(...values);
    const max = Math.max(...values);
    const range = max - min || 1;
    const bins = 15;
    const binWidth = range / bins;

    const histogram = Array(bins).fill(0);
    values.forEach(val => {
        const binIdx = Math.min(Math.floor((val - min) / binWidth), bins - 1);
        histogram[binIdx]++;
    });

    const maxFreq = Math.max(...histogram, 1);

    const padding = 60;
    const width = vizCanvas.width - 2 * padding;
    const height = vizCanvas.height - 2 * padding;
    const barWidth = width / bins;

    // Draw axes
    ctx.strokeStyle = '#333';
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(padding, padding);
    ctx.lineTo(padding, height + padding);
    ctx.lineTo(width + padding, height + padding);
    ctx.stroke();

    // Draw bars
    ctx.fillStyle = '#FF9800';
    histogram.forEach((freq, idx) => {
        const x = padding + idx * barWidth;
        const barHeight = (freq / maxFreq) * height;
        const y = height + padding - barHeight;
        ctx.fillRect(x, y, barWidth * 0.9, barHeight);
    });

    // Labels
    ctx.fillStyle = '#666';
    ctx.font = '10px Arial';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'top';
    ctx.fillText(numField, width / 2 + padding, height + padding + 10);
    
    ctx.textAlign = 'right';
    ctx.textBaseline = 'middle';
    for (let i = 0; i <= 5; i++) {
        const y = height + padding - (i * height / 5);
        const value = Math.round(i * maxFreq / 5);
        ctx.fillText(value.toString(), padding - 5, y);
    }

    if (vizMessage) vizMessage.textContent = `Histogram: ${numField} (${values.length} values, ${bins} bins)`;
}

// Add event listener for visualization type change
if (vizTypeSelect) {
    vizTypeSelect.addEventListener('change', updateVisualization);
}