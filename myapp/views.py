from django.shortcuts import render
from .calculations import calculate_x

def home(request):
    return render(request, 'myapp/home.html')

def about(request):
    return render(request, 'myapp/about.html')

def task(request):
    result_students = None
    result_x = None
    a = None

    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        if form_type == 'students':
            # Обработка задачи 1: Фильтрация студентов
            students = request.POST['students'].split()
            scores = list(map(float, request.POST['scores'].split()))
            average = sum(scores) / len(scores)
            result_students = [students[i] for i in range(len(students)) if scores[i] >= average]

        elif form_type == 'calculate_x':
            # Обработка задачи 2: Вычисление значения X
            a = request.POST.get('a')
            result_x = calculate_x(a)

    return render(request, 'myapp/task.html', {
        'result_students': result_students,
        'result_x': result_x,
        'a': a,
    })

def home(request):
    # Данные о себе
    my_data = {
        'name': 'Зеленкова Александра',
        'photo': 'my_photo.jpg',  # Путь к фото
        'email': 'mymail@email.com',
        'phone': '+7 (123) 111 11 11',
    }

    # Данные о программе
    program_data = {
        'title': 'Дизайн',
        'description': 'Программа направлена на изучение современных технологий веб-разработки.',
    }

    # Данные о руководителе
    supervisor_data = {
        'name': 'Захар День',
        'photo': 'supervisor_photo.jpg',  # Путь к фото
        'email': 'zakharday@email.com',
    }

    # Данные о менеджере
    manager_data = {
        'name': 'Петрова Алена',
        'photo': 'manager_photo.jpg',  # Путь к фото
        'email': 'pettrisimo@email.com',
    }

    # Данные о сокурсниках
    classmates_data = [
        {
            'name': 'Пшенникова Диана',
            'photo': 'classmate1.jpg',  # Путь к фото
            'email': 'diana@eamil.com',
            'phone': '+7 (111) 111-11-11',
        },
        {
            'name': 'Ляч Настя',
            'photo': 'classmate2.jpg',  # Путь к фото
            'email': 'nastya@email.com',
            'phone': '+7 (222) 222-22-22',
        },
    ]

    return render(request, 'myapp/home.html', {
        'my_data': my_data,
        'program_data': program_data,
        'supervisor_data': supervisor_data,
        'manager_data': manager_data,
        'classmates_data': classmates_data,
    })