fn filter_gifts(gift: Vec<String>) -> Vec<String> {
    if gift.len() == 0 {
        vec![""];
    }
    let mut new_vec: Vec<String> = vec![];
    for gf in gift {
        if gf.contains("#") {
            continue;
        }
        new_vec.push(gf);
    }
    new_vec
}

fn main() {
    let gift1: Vec<String> = vec![
        "ar".to_string(),
        "doll#arm".to_string(),
        "ball".to_string(),
        "#train".to_string(),
    ];

    let gift3: Vec<String> = vec!["doll#arm".to_string(), "#train".to_string()];

    let gift2: Vec<String> = vec![];

    let new_vec: Vec<String> = filter_gifts(gift1);
    let new_vec2: Vec<String> = filter_gifts(gift2);
    let new_vec3: Vec<String> = filter_gifts(gift3);

    println!("{new_vec:?} {new_vec2:?} {new_vec3:?}");
}
