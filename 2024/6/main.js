/** @param {string[]} gifts
 *  @returns {boolean} True if the gift is inside the box
 */
function inBox(box) {
    /*
     * Con slice es lo mejor porque se asegura que la parte superior como la inferior no van a estar.
     * `any()` es muy similar a some pues buscan coincidencias almenos 1.
     * osea si tiene * o su no lo tiene false, en python [1:-1] es igual que con slice(1, -1) pues es como 
     * rebanar un pan o tomar algo por revanadas. Cuando pregunta nuevamente dentro de sime, es decir en el callback
     * line toma exactamente la linea en que esta por ejemplo "#*#" que seria 1, -1 es true porque con include se da 
     * cueebta que existe dentro del string.
     * */
    console.log(box.slice(1, -1))
    return box.slice(1, -1).some(line => line.slice(1, -1).includes('*'));
}

// python example
//  any("*" in line[1:-1] for line in box[1:-1])

console.log(inBox([
  "###",
  "#*#",
  "###"
])) // true

console.log(inBox([
  "####",
  "#* #",
  "#  #",
  "####"
])) // true

console.log(inBox([
  "#####",
  "#   #",
  "#  #*",
  "#####"
])) // false

console.log(inBox([
  "#####",
  "#   #",
  "#   #",
  "#   #",
  "#####"
])) // false
