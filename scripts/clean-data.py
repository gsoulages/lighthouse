with file('../buoy_2017.txt', 'r') as oldFile, file('./new.txt', 'w') as newFile:
	lines = oldFile.readlines()
	newLines = map(lambda(line): line.replace('22+', ' 22 '), lines)                                          
	newFile.writelines(newLines)