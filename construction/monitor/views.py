from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Worker, Material, Budget
from django.db.models import Sum
from .models import Budget


# 🏠 HOME
def home(request):
    return render(request, 'home.html')


# 📁 PROJECT
def project(request):
    if request.method == "POST":
        name = request.POST.get('name')
        progress = request.POST.get('progress')

        try:
            progress = int(progress)
        except (TypeError, ValueError):
            progress = 0

        if name:
            Project.objects.create(name=name, progress=progress)

        return redirect('project')   # ✅ better than '/project/'

    data = Project.objects.all()
    return render(request, 'project.html', {'data': data})


# ✏️ EDIT PROJECT
def edit_project(request, id):
    project = get_object_or_404(Project, id=id)

    if request.method == "POST":
        project.name = request.POST.get('name')

        try:
            project.progress = int(request.POST.get('progress', 0))
        except (TypeError, ValueError):
            project.progress = 0

        project.save()
        return redirect('project')

    return render(request, 'edit.html', {'project': project})


# 🗑 DELETE PROJECT
def delete_project(request, id):
    project = get_object_or_404(Project, id=id)
    project.delete()
    return redirect('project')


# 👷 WORKER
def worker(request):
    if request.method == "POST":
        name = request.POST.get('name')
        task = request.POST.get('task')

        if name and task:
            Worker.objects.create(name=name, task=task)

        return redirect('worker')

    data = Worker.objects.all()
    return render(request, 'worker.html', {'data': data})


# 🗑 DELETE WORKER
def delete_worker(request, id):
    worker = get_object_or_404(Worker, id=id)
    worker.delete()
    return redirect('worker')


# 🧱 MATERIAL
def material(request):
    if request.method == "POST":
        name = request.POST.get('name')
        quantity = request.POST.get('quantity')

        if name and quantity:
            Material.objects.create(name=name, quantity=quantity)

        return redirect('material')

    data = Material.objects.all()
    return render(request, 'material.html', {'data': data})
def delete_material(request, id):
    obj = Material.objects.get(id=id)
    obj.delete()
    return redirect('/material/')


from .models import Budget, Project

# 🧱 BUDGET VIEW (MAIN LOGIC)
def budget(request):
    project = Project.objects.first()

    if request.method == "POST":
        desc = request.POST.get("desc")
        amount = request.POST.get("amount")

        try:
            amount = int(amount)
        except:
            amount = 0

        obj = Budget.objects.filter(project=project, desc=desc).first()

        if obj:
            obj.amount += amount
            obj.save()
        else:
            Budget.objects.create(project=project, desc=desc, amount=amount)

        # ✅ IMPORTANT: reset flag after new entry
        request.session['reset_total'] = False

        return redirect('/budget/')

    data = Budget.objects.all()

    total = data.aggregate(Sum('amount'))['amount__sum'] or 0

    # show reset only if active
    if request.session.get('reset_total'):
        total = 0

    return render(request, 'budget.html', {
        'data': data,
        'total': total
    })
# 🔄 RESET TOTAL (SOFT RESET)
def reset_budget(request):
    request.session['reset_total'] = True
    return redirect('/budget/')


# 🗑 DELETE SINGLE ITEM
def delete_budget(request, id):
    Budget.objects.get(id=id).delete()
    return redirect('/budget/')
# 📊 DASHBOARD
def dashboard(request):
    return render(request, 'dashboard.html', {
        'projects': Project.objects.count(),
        'workers': Worker.objects.count(),
        'materials': Material.objects.count(),
        'budgets': Budget.objects.count()
    })