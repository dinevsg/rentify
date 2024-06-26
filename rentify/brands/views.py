from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from rentify.brands.forms import CreateBrandForm
from rentify.brands.models import Brand
from rentify.vanilla.mixins import StaffRequiredMixin


class CreateBrandView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    template_name = "brands/brand-create.html"
    form_class = CreateBrandForm
    success_url = reverse_lazy("brands-list")


class BrandsListView(ListView):
    model = Brand
    template_name = "brands/brands-list.html"
    context_object_name = "brand"


class EditBrandView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    queryset = Brand.objects.all()
    fields = "__all__"
    template_name = "brands/brand-edit.html"

    def get_success_url(self):
        return reverse("brands-list",)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # list of attributes
        attributes = ["name", "logo", "slug",]
        # populate the context with object attributes
        context.update({attr: getattr(self.object, attr) for attr in attributes})
        return context


class DeleteBrandView(StaffRequiredMixin, DeleteView):
    model = Brand
    template_name = "brands/brand-delete.html"
    success_url = reverse_lazy("brands-list")
