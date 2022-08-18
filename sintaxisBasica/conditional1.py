print('Studen grade evaluation program')
print("Enter student's grade:")
nota_alumno = input()
def evaluation(nota):
    state = 'approved'
    if nota < 7:
        state = "not approved"
    return state

print('Alumno:', evaluation(int(nota_alumno)))
    
    