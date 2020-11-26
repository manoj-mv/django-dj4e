from django.core.exceptions import ValidationError


# validator for size limit on image field
def file_size(value): 
    limit = 500 * 1024
    if value.size > limit:
        print('size error:inside validator file_size')
        raise ValidationError('File too large. Size should not exceed 500 KB.')