from django.shortcuts import render, redirect, reverse, get_object_or_404

from notifications.models import Notification

def ShowNotifications(request):
    user = request.user

    # Prioritize requests
    notifications_type_5 = Notification.objects.filter(user=user, notification_type=5).order_by('-date')
    notifications_type_6 = Notification.objects.filter(user=user, notification_type=6).order_by('-date')
    notifications_type_7 = Notification.objects.filter(user=user, notification_type=7).order_by('-date')

    notifications_type_4 = Notification.objects.filter(user=user, notification_type=4).order_by('-date')
    notifications_type_1 = Notification.objects.filter(user=user, notification_type=1).order_by('-date')
    notifications_type_2 = Notification.objects.filter(user=user, notification_type=2).order_by('-date')
    notifications_type_3 = Notification.objects.filter(user=user, notification_type=3).order_by('-date')
    notifications_type_8 = Notification.objects.filter(user=user, notification_type=8).order_by('-date')
    notifications_type_9 = Notification.objects.filter(user=user, notification_type=9).order_by('-date')
    notifications_type_10 = Notification.objects.filter(user=user, notification_type=10).order_by('-date')



    notifications = (list(notifications_type_5) +
                     list(notifications_type_6) +
                     list(notifications_type_7) +
                     list(notifications_type_10) +
                     list(notifications_type_8) +
                     list(notifications_type_9) +
                     list(notifications_type_4) +
                     list(notifications_type_1) +
                     list(notifications_type_2) +
                     list(notifications_type_3)
                     )


    return render(request, 'notifications/notifications.html', {'notifications': notifications})


def DeleteNotification(request, id):
    user = request.user
    notification = get_object_or_404(Notification, pk=id, user=user)
    notification.delete()
    return redirect(reverse('notifications:show-notifications'))

def DeleteAllNotifications(request):
    user = request.user
    noty = Notification.objects.filter(user=user)
    noty.delete()
    return redirect(reverse('notifications:show-notifications'))


