const shoes = [
  { type: 'I', size: 38 },
  { type: 'R', size: 38 },
  { type: 'R', size: 42 },
  { type: 'I', size: 41 },
  { type: 'I', size: 42 }
]

const shoes2 = [
  { type: 'I', size: 38 },
  { type: 'R', size: 38 },
  { type: 'I', size: 38 },
  { type: 'I', size: 38 },
  { type: 'R', size: 38 }
]

const shoes3 = [
  { type: 'I', size: 38 },
  { type: 'R', size: 36 },
  { type: 'R', size: 42 },
  { type: 'I', size: 41 },
  { type: 'I', size: 43 }
]

const shoes4 = [
  { type: "I", size: 40 },
  { type: "R", size: 40 },
  { type: "I", size: 40 },
  { type: "I", size: 40 }
]


const shoes5 = [
  { type: "I", size: 40},
  { type: "R", size: 40 },
  { type: "I", size: 40 },
  { type: "I", size: 40 }
]

function organizeShoes(shoes) {
  const sizeShoes = [];

  for (let i = 0; i < shoes.length; i++) {
    console.log(i, "For de i")
    for (let e = 1; e < shoes.length; e++) {
      if (shoes[i].size === shoes[e].size && shoes[i].type !== shoes[e].type) {
        sizeShoes.push(shoes[i].size); 
        shoes.splice(e, 1);           
        shoes.splice(i, 1);
        console.log(i, "For de i dentro de for de e")   
        i--
        break
        }
    }
  }

  return sizeShoes;
}



console.log(organizeShoes(shoes))
console.log(organizeShoes(shoes2))
console.log(organizeShoes(shoes3))
console.log(organizeShoes(shoes4))
console.log(organizeShoes(shoes5))

