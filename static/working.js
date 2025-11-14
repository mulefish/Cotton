const selectEl = document.getElementById('selecter');
const selectionSummary = document.getElementById('selectionSummary');
const tableBody = document.querySelector('#selectionTable tbody');
const tableHeadRow = document.getElementById('selectionHeaderRow');
const fetchButton = document.getElementById('fetchBtn');
const errorMessage = document.getElementById('errorMessage');
const selectedValues = new Set();
const defaultFields = ['colorGrade', 'leafGrade', 'stapleCode'];

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

function renderTableHeader(fields) {
    tableHeadRow.innerHTML = '';
    fields.forEach(field => {
        const th = document.createElement('th');
        th.textContent = field;
        tableHeadRow.appendChild(th);
    });
    const countHeader = document.createElement('th');
    countHeader.textContent = 'count';
    tableHeadRow.appendChild(countHeader);
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
    return selectedValues.size ? Array.from(selectedValues) : defaultFields;
}

async function fetchData() {
    errorMessage.textContent = '';
    const pendingFields = currentFields();
    renderTableHeader(pendingFields);
    renderResults([], pendingFields);

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
        const fields = (payload.requestedFields && payload.requestedFields.length)
            ? payload.requestedFields
            : defaultFields;
        renderTableHeader(fields);
        renderResults(payload.summary || [], fields);
    } catch (err) {
        errorMessage.textContent = `Error fetching data: ${err.message}`;
    }
}

selectEl.addEventListener('change', updateSelection);
fetchButton.addEventListener('click', fetchData);
renderSelectionSummary();
renderTableHeader(defaultFields);
renderResults([], defaultFields);