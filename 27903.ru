c = [9*9+25-6+9, 9*9+25-6+5, 9*9+25-6+5+5+5, 9*9+25-6+5+5+5+5-4, 6*8, 11*5, 5*5*2+4-5, 5*5*2+5-4]

w = 0
loop do
  r += c[w].chr
  w += 1
  r += c[w].chr
  w += 1
  r += c[w].chr
  w += 1
  r += c[w].chr
  w += 1
  r += c[w].chr
  w += 1
  r += c[w].chr
  w += 1
  r += c[w].chr
  w += 1
  r += c[w].chr
  w += 1
  
  z = 0
  c.each { z += 1 }

  break if w >= z
end

$> << r