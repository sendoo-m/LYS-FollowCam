building_1_group, created = Group.objects.get_or_create(name='Abo Bakr')
building_1_view_permission = Permission.objects.get(name='Can view Abo Bakr')
building_1_group.permissions.add(building_1_view_permission)
building_1_group.save()

building_2_group, created = Group.objects.get_or_create(name='Administrator Build')
building_2_view_permission = Permission.objects.get(name='Can view Administrator Build')
building_2_group.permissions.add(building_2_view_permission)
building_2_group.save()

building_3_group, created = Group.objects.get_or_create(name='KG')
building_3_view_permission = Permission.objects.get(name='Can view KG')
building_3_group.permissions.add(building_3_view_permission)
building_3_group.save()

building_4_group, created = Group.objects.get_or_create(name='New American')
building_4_view_permission = Permission.objects.get(name='Can view New American')
building_4_group.permissions.add(building_4_view_permission)
building_4_group.save()

building_5_group, created = Group.objects.get_or_create(name='American')
building_5_view_permission = Permission.objects.get(name='Can view American')
building_5_group.permissions.add(building_5_view_permission)
building_5_group.save()

building_6_group, created = Group.objects.get_or_create(name='Moaaz')
building_6_view_permission = Permission.objects.get(name='Can view Moaaz')
building_6_group.permissions.add(building_6_view_permission)
building_6_group.save()

building_7_group, created = Group.objects.get_or_create(name='Prep and Secondary')
building_7_view_permission = Permission.objects.get(name='Can view Prep and Secondary')
building_7_group.permissions.add(building_7_view_permission)
building_7_group.save()
