from django.shortcuts import render, redirect, reverse, get_object_or_404

from notifications.models import Notification

def ShowNotifications(request):
    user = request.user
    notifications = Notification.objects.filter(user=user).order_by('-date')

    return render(request, 'notifications/notifications.html', {'notifications': notifications})


def DeleteNotification(request, id):
    user = request.user
    notification = get_object_or_404(Notification, pk=id, user=user)
    notification.delete()
    return redirect(reverse('notifications:show-notifications'))


