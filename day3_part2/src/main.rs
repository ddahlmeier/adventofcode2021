use std::env;
use std::fs;
use std::io::{BufRead, BufReader};

/// Compute diagnostic report from binary input.


fn bit_criteria(count_ones: f64, total: f64, rating: &str) -> u32 {
	if rating == "oxygen" {
		if count_ones >= total/2.0 {
    	   	return 1;
    	} else {
    		return 0;
    	}
    } else if rating == "co2" {
    	if count_ones < total/2.0 {
    	    return 1;
    	} else {
    		return 0;
    	}
    } else {
    	println!("Unknown report type");
    	return 0;
    }
}

fn filter_report(mut report: Vec<Vec<u32>>, rating: &str) -> i32 {
    let col_count = report[0].len();

    for idx in 0..col_count {
        let mut count_ones: f64 = 0.0;
        let row_count = report.len() as f64;
        for line in report.iter() {
           count_ones += line[idx] as f64;
        }
        let bit = bit_criteria(count_ones, row_count, rating);       
        report = report.into_iter().filter(|x| x[idx] == bit).collect::<Vec<_>>();
 	    if report.len() < 2 {
 	    	break;
 	    }
 	}
 	let result_str: String = report[0].iter().map(|i| i.to_string()).collect::<String>();
 	let result = i32::from_str_radix(&result_str, 2).unwrap();
 	return result;
}


fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() != 2 {
        eprintln!("Usage day3_part2 <input_file>");
        std::process::exit(1);
    }
    let file = fs::File::open(&args[1]).unwrap();
    let reader = BufReader::new(file);
    let mut report: Vec<Vec<u32>> = Vec::new();

    for line in reader.lines() {
        let line = line.unwrap();
        let mut bits: Vec<u32> = Vec::new();
        for bit in line.chars() {
            bits.push(bit.to_digit(10).unwrap());
        }
        report.push(bits);
    }
    let oxygen_generator_reading = filter_report(report.clone(), "oxygen");
    let co2_scrubber_rating = filter_report(report.clone(), "co2");  
    println!("{}", oxygen_generator_reading*co2_scrubber_rating);
}
