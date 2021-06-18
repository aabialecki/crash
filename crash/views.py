from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib import messages
from .forms import betForm
from .game import *
from users.models import Stats
import ast




def index(request):
    return render(request, 'crash/index.html')

@login_required
def game(request):
    game_msg = {'isWinner':None,
                'bet':0,
                'multiplier':0,
                'winnings':0}
    user = request.user

    storage = messages.get_messages(request)
    for message in storage:
        game_msg=message
        break

    if request.method == 'POST':
        form = betForm(request.POST, user=request.user)
        if form.is_valid():
            bet = form.cleaned_data.get('bet')
            multiplier = form.cleaned_data.get('multiplier')
            isWinner = start_game(multiplier)
            if isWinner['won']:
                winnings = (multiplier*bet)-bet
            else:
                winnings = 0-bet
            user.stats.balance+=winnings
            user.stats.save()
            game_msg = {'isWinner':str(isWinner['won']),
                        'bet':bet,
                        'multiplier':multiplier,
                        'winnings':round(abs(winnings),2),
                        'crash_multiplier':round(isWinner['multiplier'],2)}
            messages.add_message(request, messages.INFO, game_msg)
            return redirect('game')
    else:
        form = betForm(user=request.user)

    game_msg = ast.literal_eval(str(game_msg))
    return render(request, 'crash/game.html', {'form': form,
                                                   'game_msg': game_msg})
