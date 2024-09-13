from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "loose at least 5 kg",
    "february": "climb 8a+",
    "march": "learn crack climbing",
    "april": "find a solid climbing partner",
    "may": "spend some time outdoors doing trad",
    "june": "go for an alpine climbing",
    "july": "go once again for alpine climbing",
    "august": "reset, double think your priorities",
    "september": "plan a trip to yosemite while training hard",
    "october": "go to yosemite",
    "november": "send the Freerider route on El Cap",
    "december": "celebrate, relax, reorganize, climb harder",
}


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(
            request,
            "challenges/challenge.html",
            {"text": challenge_text, "month": month},
        )
    except:
        raise Http404()


def challenges(request):
    months = monthly_challenges.keys()
    return render(request, "challenges/index.html", {"months": months})
