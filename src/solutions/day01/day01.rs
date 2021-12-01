fn get_numbers(file_content: &str) -> Vec<usize> {
    file_content
        .lines()
        .map(|line| line.parse::<usize>().expect("Can't parse number"))
        .collect::<Vec<usize>>()
}

fn generic_solution(numbers: &Vec<usize>, window_size: usize) -> usize {
    numbers
        .windows(window_size)
        .collect::<Vec<&[usize]>>()
        .windows(2)
        .into_iter()
        .filter(|windows| windows[0][0] < windows[1][windows[1].len() - 1])
        .count()
}

pub fn day01() {
    println!("Solutions for test.txt:");
    let numbers = get_numbers(include_str!("../../inputs/day01/test.txt"));
    println!("Part 1 {}", generic_solution(&numbers, 1));
    println!("Part 2 {}", generic_solution(&numbers, 3));

    println!("Solutions for day01.txt:");
    let numbers = get_numbers(include_str!("../../inputs/day01/sol.txt"));
    println!("Part 1 {}", generic_solution(&numbers, 1));
    println!("Part 2 {}", generic_solution(&numbers, 3));
}
