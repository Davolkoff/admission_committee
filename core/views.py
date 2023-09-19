import time

from django.shortcuts import render, redirect
from .models import MenuButtons, Pages, Operators, Tickets, Experts
from .image_generator import generate_ticket, generate_expert_ticket
import os
from ip_tool import get_local_ip




# функция старта
def start_page(request):
    ip = get_local_ip() + ":7777"
    return render(request, 'core/start_page.html', {'ip_addr': ip})


# функция для вывода кнопок в соответствии с полученным значением page_id
def page_view(request, page_id=0):
    pages = Pages.objects.filter(page_id=page_id)

    if len(pages) > 0:
        page = pages[0]
        buttons = MenuButtons.objects.filter(page=page)
        num_of_buttons = len(buttons)
        if num_of_buttons < 3:
            num_of_buttons = 3
        return render(request, 'core/index.html', {'buttons': buttons, 'page': page, 'num_of_buttons': num_of_buttons})
    else:
        return render(request, 'core/index.html')




# функция для вывода оператора окна
def operator_view(request, operator_id):
    operator_info = Operators.objects.filter(window_number=operator_id)

    if len(operator_info):
        operator = operator_info[0]
        if not operator.current_ticket:
            first_ticket = Tickets.objects.filter(taken=False).first()
            if first_ticket is not None and not first_ticket.ticket_id == -1 and first_ticket.question == 'Подать заявление' :
                window_number = operator.window_number
                ticket_id = first_ticket.ticket_id
                ticket_question = first_ticket.question
                operator.current_ticket = first_ticket
                first_ticket.taken = True
                first_ticket.save()
                operator.save()
            else:
                ticket_id = "-"
                window_number = operator.window_number
                ticket_question = "Очередь пуста"
        else:
            ticket_id = operator.current_ticket.ticket_id
            ticket_question = operator.current_ticket.question
            if ticket_id == -1:
                ticket_id = "-"
                ticket_question = "-"
            window_number = operator.window_number
    else:
        ticket_question = "-"
        ticket_id = "-"
        window_number = "-"
    return render(request, "core/operator_interface.html", {'ticket_question': ticket_question, 'ticket_id': ticket_id,
                                                            'window_number': window_number})

def expert_view(request, expert_id):
    expert_info = Experts.objects.filter(window_number=expert_id)

    if len(expert_info):
        expert = expert_info[0]
        if not expert.current_ticket:
            first_ticket = Tickets.objects.filter(taken=False).first()
            if first_ticket is not None and not first_ticket.ticket_id == -1 and not first_ticket.question == 'Подать заявление':
                window_number = expert.window_number
                ticket_id = first_ticket.ticket_id
                ticket_question = first_ticket.question
                expert.current_ticket = first_ticket
                first_ticket.taken = True
                first_ticket.save()
                expert.save()
            else:
                ticket_id = "-"
                window_number = expert.window_number
                ticket_question = "Очередь пуста"
        else:
            ticket_id = expert.current_ticket.ticket_id
            ticket_question = expert.current_ticket.question
            if ticket_id == -1:
                ticket_id = "-"
                ticket_question = "-"
            window_number = expert.window_number
    else:
        ticket_question = "-"
        ticket_id = "-"
        window_number = "-"
    return render(request, "core/expert_interface.html", {'ticket_question': ticket_question, 'ticket_id': ticket_id,
                                                            'window_number': window_number})



# функция для завершения обработки текущего посетителя
def ticket_ready(request, operator_id):
    operator_info = Operators.objects.filter(window_number=operator_id)
    if len(operator_info):
        operator = operator_info[0]
        operator.current_ticket = None
        operator.save()
    return redirect(f"/operator/{operator_id}")

def expert_ticket_ready(request, expert_id):
    expert_info = Experts.objects.filter(window_number=expert_id)
    if len(expert_info):
        expert = expert_info[0]
        expert.current_ticket = None
        expert.save()
    return redirect(f"/expert/{expert_id}")


# функция, отвечающая за обработку человека без талона
def without_ticket(request, operator_id):
    operator_info = Operators.objects.filter(window_number=operator_id)
    if len(operator_info):
        operator = operator_info[0]
        operator.current_ticket = Tickets.objects.get(ticket_id=-1)
        operator.save()
    return redirect(f"/operator/{operator_id}")

def expert_without_ticket(request, expert_id):
    expert_info = Experts.objects.filter(window_number=expert_id)
    if len(expert_info):
        expert = expert_info[0]
        expert.current_ticket = Tickets.objects.get(ticket_id=-1)
        expert.save()
    return redirect(f"/expert/{expert_id}")

def void_view(request):
    return render(request, "core/void.html")

# функция для печати наклейки в соответствии с нажатой кнопкой
def print_sticker(request, page_id, button_id):
    void_view(request)
    pages = Pages.objects.filter(page_id=page_id)
    
    if len(pages) > 0:
        page = pages[0]
        buttons = MenuButtons.objects.filter(page=page, button_id=button_id)
        if len(buttons) > 0:
            button = buttons[0]
            if button.print_file == 'pic1.png':
                last_ticket = Tickets.objects.last()
                if last_ticket != None:
                    new_ticket = last_ticket.ticket_id+1
                else:
                    new_ticket = 0

                Tickets.objects.create(ticket_id=new_ticket, question=button.text)
                    
                generate_ticket(new_ticket)
                time.sleep(0.5)

            elif button.print_file == 'pic2.png':
                last_ticket = Tickets.objects.last()
                if last_ticket != None:
                    new_ticket = last_ticket.ticket_id+1
                else:
                    new_ticket = 0

                Tickets.objects.create(ticket_id=new_ticket, question=button.text)
                    
                generate_expert_ticket(new_ticket)
                time.sleep(0.5)


        
        temp = os.path.abspath(f"core/img/{button.print_file}")
    
        os.system(f"C:\\IrfanView.lnk \"{temp}\" /print")
    return render(request, "core/void.html")




# информация о текущем талончике у окна для большого экрана
def queue_view(request, operator_id):
    operator_info = Operators.objects.filter(window_number=operator_id)

    if len(operator_info):
        operator = operator_info[0]
        window_number = operator.window_number
        if not operator.current_ticket or operator.current_ticket.ticket_id == -1:
            ticket_id = "-"
        else:
            ticket_id = operator.current_ticket.ticket_id
    else:
        ticket_id = "-"
        window_number = "-"
    return render(request, "core/queue_interface.html", {'ticket_id': ticket_id,
                                                            'window_number': window_number})

def all_queue_view(request):
    operators = Operators.objects.all()
    experts = Experts.objects.all()
    return render(request, "core/queue_all.html", {'operators': operators, 'experts': experts})
