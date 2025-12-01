/**
  * @param {Array<Object>} data
  * @returns {string}
  */
function drawTable(data) {

  const columnas = Object.keys(data[0]);

  const ancho = columnas.map(col => {
    return Math.max(
      col.length,
      ...data.map(row => (row[col].toString()).length)
    );
  });

    console.log(ancho)

}

drawTable([
  { name: 'Alice', city: 'London' },
  { name: 'Bob', city: 'Paris' },
  { name: 'Charlie', city: 'New York' },
  { name: 'Jakepysp', city: 'Mosscu jijijia'}
])
// +---------+-----------+
// | Name    | City      |
// +---------+-----------+
// | Alice   | London    |
// | Bob     | Paris     |
// | Charlie | New York  |
// +---------+-----------+


drawTable([
  { gift: 'Doll', quantity: 10 },
  { gift: 'Book', quantity: 5 },
  { gift: 'Music CD', quantity: 1 }
])

// +----------+----------+
// | Gift     | Quantity |
// +----------+----------+
// | Doll     | 10       |
// | Book     | 5        |
// | Music CD | 1        |
// +----------+----------+

