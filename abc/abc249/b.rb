S = gets
 
hash = {}
 
S.chars { |char|
  unless ('A'..'Z').include?(char)
    puts 'No'
    return
  end
  unless ('a'..'z').include?(char)
    puts 'No'
    return
  end
  
  if hash[char].present?
    hash[char] += 1
  else
    hash[char] = 1
  end  
}
 
  
hash.each{|key, value|
  if value > 1
    puts 'No'
    return
  end
}
puts 'Yes'