import random

images = [
    "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Cat_November_2010-1a.jpg/330px-Cat_November_2010-1a.jpg", 
    "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Felis_silvestris_silvestris_Luc_Viatour.jpg/255px-Felis_silvestris_silvestris_Luc_Viatour.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSdMZZ7e1h5Z3CND86yYzplFKj1EHWuKpiysQ&s",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSGBZOZ9mXhpyjt8aPoBQxmdkMf4JLVEJRehQ&s",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ9-kG-NOsfz65U6AjmM8JrPQqaChGVtFyVUA&s",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQMsRFA_8onp5XlC3wIbih5tvQ2Y1j6xvSvVg&s",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSI66jee7bxwQrCaPoVbOBV-WhJpGjXstXFxw&s",
    
]

i = random.randint(0, len(images) - 1)
selected = images[i]