type Board = string
type Moves = string
type Result = 'fail' | 'crash' | 'success'

function moveReno(board: Board, moves: Moves): Result {
    const lines = board.split('\n').slice(1, -1);

    let renoRow = -1;
    let renoCol = -1;

    for (let i = 0; i < lines.length; i++) {
        const col = lines[i].indexOf('@');
        if (col !== -1) {
            renoRow = i;
            renoCol = col;
            break;
        }
    }

    let collected = false;

    for (const move of moves) {
        let newRow = renoRow;
        let newCol = renoCol;

        if (move === 'U') {
            newRow--;
        } else if (move === 'D') {
            newRow++;
        } else if (move === 'L') {
            newCol--;
        } else if (move === 'R') {
            newCol++;
        }

        if (newRow < 0 || newRow >= lines.length) {
            return collected ? 'success' : 'crash';
        }

        if (newCol < 0 || newCol >= lines[newRow].length) {
            return collected ? 'success' : 'crash';
        }

        const cell = lines[newRow][newCol];

        if (cell === '#') {
            return collected ? 'success' : 'crash';
        }

        if (cell === '*') {
            collected = true;
        }

        renoRow = newRow;
        renoCol = newCol;
    }

    return collected ? 'success' : 'fail';

}

const board = `
.....
.*#.*
.@...
.....
`

console.log(moveReno(board, 'D')); // ➞ 'fail' -> se mueve pero no recoge nada
console.log(moveReno(board, 'U')); // ➞ 'Sussces'
console.log(moveReno(board, 'RU')); // ➞ 'Crash'
console.log(moveReno(board, 'RRRUU')); // ➞ 'Sussces'
console.log(moveReno(board, 'DD')); // ➞ 'Crash'
console.log(moveReno(board, 'UUU')); // ➞ Susseces'
console.log(moveReno(board, 'RR')); // ➞ 'Fail