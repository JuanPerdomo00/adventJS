import gleam/int
import gleam/io
import gleam/list

pub fn prepare_gifts(gifrs: List(Int)) -> List(Int) {
  // Gt - the value is larger than the other value.
  // Eq - the value is equal to the other value.
  // Lt - the value is smaller than the other value.

  list.sort(gifrs, by: int.compare)
}

pub fn main() {
  let caseone: List(Int) = [3, 1, 2, 3, 4, 2, 5]
  let result = prepare_gifts(caseone)
  io.debug(result)
}
