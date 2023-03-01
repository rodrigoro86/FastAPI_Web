from fastapi.routing import APIRouter
from fastapi.requests import Request
from core.configs import settings

router = APIRouter()

@router.get('/', name='index')
async def index(request: Request):
    context = {
        "request": request
    }
    return settings.TEMPLATES.TemplateResponse('home/index.html', context=context)

@router.get('/about', name='about')
async def about(request: Request):
    context = {
        "request": request
    }
    return settings.TEMPLATES.TemplateResponse('about/index.html', context=context)

@router.get('/contact', name='contact')
async def contact(request: Request):
    context = {
        "request": request
    }
    return settings.TEMPLATES.TemplateResponse('contact/index.html', context=context)

@router.get('/pricing', name='pricing')
async def pricing(request: Request):
    context = {
        "request": request
    }
    return settings.TEMPLATES.TemplateResponse('pricing/index.html', context=context)

@router.get('/faq', name='faq')
async def faq(request: Request):
    context = {
        "request": request
    }
    return settings.TEMPLATES.TemplateResponse('faq/index.html', context=context)

@router.get('/blog/blog_home', name='blog_home')
async def blog_home(request: Request):
    context = {
        "request": request
    }
    return settings.TEMPLATES.TemplateResponse('blog/blog_home/index.html', context=context)

@router.get('/blog/blog_post', name='blog_post')
async def blog_post(request: Request):
    context = {
        "request": request
    }
    return settings.TEMPLATES.TemplateResponse('blog/blog_post/index.html', context=context)

@router.get('/portifolio/portifolio_item', name='portifolio_item')
async def portifolio_item(request: Request):
    context = {
        "request": request
    }
    return settings.TEMPLATES.TemplateResponse('portifolio/portifolio_item/index.html', context=context)

@router.get('/portifolio/portifolio_overview', name='portifolio_overview')
async def portifolio_overview(request: Request):
    context = {
        "request": request
    }
    return settings.TEMPLATES.TemplateResponse('portifolio/portifolio_overview/index.html', context=context)

