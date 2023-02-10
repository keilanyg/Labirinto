import csv, os

def get_maze(file):
    f = open(file, 'r')
    reader = csv.reader(f)
    maze = []

    for line in reader:
        maze.append(line)
    return maze

def display_maze(m, path):
    m2= m[:]
    os.system('clear')

    draw =""

    for row in m2:
        for item in row:
            item = str(item).replace("1","#")
            item = str(item).replace("0"," ")
        
            draw += item
        draw = "\n" 

    print(draw)

def move(path):
     cur = path[-1]


maze = get_maze('lab.csv')
move(((1,0),))
display_maze(maze,[])

print (maze)