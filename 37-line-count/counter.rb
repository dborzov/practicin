def count_file_lines(file_path)
  line_number = 0
  File.open(file_path, "rb") do |input_file|
    while input_file.gets
      line_number += 1
    end
  end
  line_number
end

puts count_file_lines("lines.txt")
