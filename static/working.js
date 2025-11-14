const selectEl = document.getElementById('selecter');
const selectionSummary = document.getElementById('selectionSummary');
const tableBody = document.querySelector('#selectionTable tbody');
const tableHeadRow = document.getElementById('selectionHeaderRow');
const fetchButton = document.getElementById('fetchBtn');
const errorMessage = document.getElementById('errorMessage');
const limitSelect = document.getElementById('limit');
const rotateToggle = document.getElementById('rotateToggle');
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
    rows.forEach((rowData) => {
        const row = document.createElement('tr');
        fields.forEach(field => {
            const cell = document.createElement('td');
            cell.textContent = rowData[field] ?? '';
            row.appendChild(cell);
        });
        const countCell = document.createElement('td');
        countCell.textContent = rowData.count ?? 0;
        row.appendChild(countCell);
        tableBody.appendChild(row);
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

function rerender() {
    if (!latestFields.length) {
        return;
    }
    const threshold = currentCountThreshold();
    const filtered = latestSummary.filter(item => (item.count ?? 0) >= threshold);
    const sorted = applySort(filtered);
    renderTableHeader(latestFields);
    renderResults(sorted, latestFields);
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
renderSelectionSummary();