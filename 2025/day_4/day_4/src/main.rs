fn decode_santa_pin(code: String) -> Vec<i16> {
    let cleaned = code.replace(['[', ']'], "");
    let pin: &str = &cleaned;
    let chars_pin: Vec<char> = pin.chars().collect();
    let mut nums = Vec::new();
    let mut i = 0;

    while i < chars_pin.len() {
        if chars_pin[i].is_numeric() {
            let num = (chars_pin[i] as u8 - b'0') as i16;

            i += 1;

            let mut add = 0;
            let mut sub = 0;

            while i < chars_pin.len() && chars_pin[i] == '+' {
                add += 1;
                i += 1;
            }
            while i < chars_pin.len() && chars_pin[i] == '-' {
                sub += 1;
                i += 1;
            }

            let mut resul = num + add - sub;

            if resul < 0 {
                resul = (resul % 10 + 10) % 10;
            } else {
                resul %= 10;
            }

            nums.push(resul);
        } else if chars_pin[i] == '<' {
            if !nums.is_empty() {
                nums.push(nums[nums.len() - 1]);
            }
            i += 1;
        }
    }
    nums
}

fn main() {
    println!("{:?}", decode_santa_pin("[1++][2-][3+][<]".to_string()));
    println!("{:?}", decode_santa_pin("[9+][0-][4][<]".to_string()));
}
