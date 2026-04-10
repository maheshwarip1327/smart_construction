from django.shortcuts import render, redirect
from .models import Project, Worker, Material, Budget

def home(request):
    return render(request, 'home.html')

def project(request):
    if request.method == "POST":
        name = request.POST['name']
        progress = request.POST['progress']
        Project.objects.create(name=name, progress=progress)
        return redirect('/project/')
    
    data = Project.objects.all()
    return render(request, 'project.html', {'data': data})

def worker(request):
    if request.method == "POST":
        name = request.POST['name']
        task = request.POST['task']
        Worker.objects.create(name=name, task=task)
        return redirect('/worker/')
    
    data = Worker.objects.all()
    return render(request, 'worker.html', {'data': data})
def convert_amount(value):
    value = value.lower().strip()

    if "k" in value:
        return int(float(value.replace("k", "")) * 1000)

    elif "lakh" in value or "lks" in value or "lk" in value:
        value = value.replace("lakh", "").replace("lks", "").replace("lk", "")
        return int(float(value) * 100000)

    elif "cr" in value:
        return int(float(value.replace("cr", "")) * 10000000)

    else:
        return int(value)


def budget(request):
    if request.method == 'POST':
        amount_input = request.POST.get('amount')
        desc = request.POST.get('desc')

        try:
            amount = convert_amount(amount_input)

            Budget.objects.create(
                amount=amount,
                desc=desc
            )

        except Exception as e:
            print("ERROR:", e)   # 🔥 debugging

    data = Budget.objects.all()

    total = sum(i.amount for i in data)

    return render(request, 'budget.html', {
        'data': data,
        'total': total
    })
def material(request):
    if request.method == "POST":
        name = request.POST['name']
        quantity = request.POST['quantity']
        Material.objects.create(name=name, quantity=quantity)
        return redirect('/material/')
    
    data = Material.objects.all()
    return render(request, 'material.html', {'data': data})


def dashboard(request):
    projects = Project.objects.count()
    workers = Worker.objects.count()
    materials = Material.objects.count()
    budgets = Budget.objects.count()

    return render(request, 'dashboard.html', {
        'projects': projects,
        'workers': workers,
        'materials': materials,
        'budgets': budgets
    })