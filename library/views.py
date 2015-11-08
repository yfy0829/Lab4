#-*- coding: UTF-8 -*- 。
from django.http import HttpResponse
from django.template import Context
from library.models import *
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect


def add_book(request):
     if request.method == 'POST':
        post = request.POST
        new_book = Book(
            isbn = post["isbn"],
            authorID = post["authorID"],
            title = post["title"],
            publisher = post["publisher"],
            publishdate = post["publishdate"],
            price = post["price"]  ) 
        new_book.save()
        new_author = Author.objects.filter(authorID = new_book.authorID)
        if new_author.exists():
            return render_to_response("ok.html",context_instance=RequestContext(request))
        else:  #作者不存在，添加作者
            return HttpResponseRedirect("/add_author/")            
            #return render_to_response("insert.html",context_instance=RequestContext(request))
     else:       
         return render_to_response("form.html",context_instance=RequestContext(request))
        
def add_author(request):
     if request.method == 'POST':
        post = request.POST
        new_author = Author(
            authorID = post["authorID"],
            name = post["name"],
            age = post["age"],
            country = post["country"]) 
        new_author.save()
        return render_to_response("ok.html",context_instance=RequestContext(request))
     else:
        return render_to_response("add_author.html",context_instance=RequestContext(request))


def update(request):  #更新书的内容 
    isbn = request.GET["isbn"]
    book=Book.objects.get(isbn=isbn)
    c = RequestContext(request,{"book":book})
    if request.method == 'POST':
        post = request.POST
        book.isbn = post["isbn"]
        book.authorID= post["authorID"]
        book.title = post["title"]
        book.publisher = post["publisher"]
        book.publishdate = post["publishdate"]
        book.price = post["price"]   
        book.save()
        return render_to_response("ok.html",context_instance=RequestContext(request))
    else:
        return render_to_response("update.html",c)
    
def search_form(request):
    return render_to_response("search_form.html")  #搜索框

def search(request):    
    name = request.GET["name"]   
    author = Author.objects.filter(name = name)  #列表
    if author.exists():
        book = Book.objects.filter(authorID = author[0].authorID)
        for i in range (1,len(author)):
            book = book|Book.objects.filter(authorID = author[i].authorID) #合并两个QuerySet
        if book.exists():
            c = Context({"book":book})        #字典
            return render_to_response("search.html",c)
        else:
            return render_to_response("no_book.html",context_instance=RequestContext(request))
    else:
        return render_to_response("no_writer.html",context_instance=RequestContext(request)) 
        

def book_view(request): #书的详细信息
     title = request.GET["title"]    
     book = Book.objects.filter(title = title)
     author = Author.objects.filter(authorID = book[0].authorID)
     c = Context({"book":book,"author":author})   
     return render_to_response("book_view.html", c)
     
def delete(request): #书删除
    isbn = request.GET["isbn"]
    book=Book.objects.get(isbn = isbn)
    book.delete()
    return render_to_response("delete.html",isbn)

