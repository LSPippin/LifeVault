from vault.models import Category


def categories(request):
    if request.user.is_authenticated:
        return {
            'nav_categories': Category.objects.filter(user=request.user)
        }
    return {}
