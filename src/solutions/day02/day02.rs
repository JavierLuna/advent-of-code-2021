fn solution_1(file_content: &str) -> usize {
    let mut depth = 0;
    let mut horizontal = 0;
    for line in file_content.lines() {
        let split_line: Vec<&str> = line.trim().split(" ").collect();
        let instruction = split_line[0];
        let value = split_line[1].parse::<usize>().expect("Cannot parse value");

        match instruction {
            "forward" => horizontal += value,
            "down" => {
                depth += value;
            }
            "up" => {
                depth -= value;
            }
            _ => {
                println!("Unknown operation!!")
            }
        }
    }
    return depth * horizontal;
}

fn solution_2(file_content: &str) -> usize {
    let mut depth = 0;
    let mut horizontal = 0;
    let mut aim = 0;
    for line in file_content.lines() {
        let split_line: Vec<&str> = line.trim().split(" ").collect();
        let instruction = split_line[0];
        let value = split_line[1].parse::<usize>().expect("Cannot parse value");

        match instruction {
            "forward" => {
                horizontal += value;
                depth += aim * value;
            }
            "down" => {
                aim += value;
            }
            "up" => {
                aim -= value;
            }
            _ => {
                println!("Unknown operation!!")
            }
        }
    }
    return depth * horizontal;
}

pub fn day02() {
    println!("Solutions for test.txt:");
    let content = include_str!("../../inputs/day02/test.txt");
    println!("Part 1 {}", solution_1(content));
    println!("Part 2 {}", solution_2(content));

    println!("Solutions for sol.txt:");
    let content = include_str!("../../inputs/day02/sol.txt");
    println!("Part 1 {}", solution_1(content));
    println!("Part 2 {}", solution_2(content));
}
