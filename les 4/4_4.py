def new_password(new_password, old_password):
    if new_password != old_password and len(new_password)>6:
        return True
    else:
        return False
print(new_password('dkofogko','cfngfhncon'))








