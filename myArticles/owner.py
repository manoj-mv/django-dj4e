# File that implements owner rows. ie, user can prform crud operation only on the data they own

from django.views.generic import CreateView,UpdateView,DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin

# ListView and DetailView remains the same,They only handles get request

class OwnerCreateView(LoginRequiredMixin, CreateView):
    """
    Sub-class of the CreateView to automatically pass the Request to the Form
    and add the owner to the saved object.
    """


    # Saves the form instance, sets the current object for the view, and redirects to get_success_url().
    def form_valid(self,form):
        print('form valid called')
        object = form.save(commit=False)
        object.owner = self.request.user
        object.save()
        return super(OwnerCreateView,self).form_valid(form)

class OwnerUpdateView(LoginRequiredMixin, UpdateView):
    """
    Sub-class the UpdateView to pass the request to the form and limit the
    queryset to the requesting user.
    """
    def get_queryset(self):
        print('update get_query_setr is called')
        qs = super(OwnerUpdateView,self).get_queryset()
        return qs.filter(owner=self.request.user)


class OwnerDeleteView(LoginRequiredMixin,DeleteView):
    """
    Sub-class the DeleteView to restrict a User from deleting other
    user's data.
    """
    def get_queryset(self):
        print('delete get_query_set is called')
        qs = super(OwnerDeleteView,self).get_queryset()
        return qs.filter(owner=self.request.user)




