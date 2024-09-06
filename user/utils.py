from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import render, redirect


class SteamURLRequiredMixin(AccessMixin):
    """Этот миксин проверяет, привязан ли у пользователя steamurl."""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        if not request.user.check_auth():
            # Если steamurl не привязан, отображаем страницу с предупреждением
            return render(request, 'check_auth_user.html', context={'user': request.user})

        if not request.user.check_status():
            return render(request, 'check_status_user.html', context={'user': request.user})
        return super().dispatch(request, *args, **kwargs)
