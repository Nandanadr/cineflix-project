from django.shortcuts import render,redirect

from django.views import View

from .models import Movie,IndustryChoices,ArtistChoices,GenreChoices,LanguageChoices,CertificationChoices

from .forms import MovieForm

from django.db.models import Q

from django.utils.decorators import method_decorator

from authentication.permissions import permitted_user_roles

from cineflix.utils import get_recommended_movies

from subscriptions.models import UserSubscription

from django .contrib import messages

# Create your views here.

class HomeView(View):

    template = 'home.html'

    def get(self,request,*args,**kwargs):

        data ={'page':'home'}

        return render(request,self.template,context=data)
    
class MoviesListVeiw(View):

    template = 'movies/movie-list.html'

    def get(self,request,*args,**kwargs):

        movies = Movie.objects.filter(active_status=True)

        data = {'page':'Movies','movies':movies}

        return render(request,self.template,context=data)
    
# class MovieCreateView(View):

#     def get(self,request,*args,**kwargs):

#         industry_choices = IndustryChoices

#         genre_choices = GenreChoices

#         language_choices = LanguageChoices

#         artist_choices = ArtistChoices

#         certification_choices = CertificationChoices


#         data = {'page':'Create Movies',
#                 'industry_choices':IndustryChoices,
#                 'genre_choices':GenreChoices,
#                 'language_choices':LanguageChoices,
#                 'artist_choices':ArtistChoices,
#                 'certification_choices':CertificationChoices}

#         return render(request,'movies/movie-create.html',context=data)
    
#     def post(self,request,*args,**kwargs):

#         movie_data = request.POST

#         name = movie_data.get('name')

#         photo = request.FILES.get('photo')

#         description = movie_data.get('description')

#         release_date = movie_data.get('release_date')

#         industry = movie_data.get('industry')

#         runtime = movie_data.get('runtime')

#         certification = movie_data.get('certification')

#         genre = movie_data.get('genre')

#         artists = movie_data.get('artists')

#         video = movie_data.get('video')

#         tags = movie_data.get('tags')

#         languages = movie_data.get('languages')

#         print(name)

#         print(photo)

#         print(description)

#         print(release_date)

#         print(industry)

#         print(runtime)

#         print(certification)
        
#         print(genre)

#         print(artists)
        
#         print(video)

#         print(tags)

#         print(languages)

#         Movie.objects.create(name=name,photo=photo,description=description,release_date=release_date,industry=industry,runtime=runtime,certification=certification,genre=genre,artists=artists,video=video,tags=tags,languages=languages)


#         return redirect('movie-list')

@method_decorator(permitted_user_roles(['Admin']),name='dispatch')

class MovieCreateView(View):

    form_class = MovieForm

    template = 'movies/movie-create.html'

    def get(self,request,*args,**kwargs):
        
        form = self.form_class()

        data = {'page':'Create Movie',
                'form':form}

        return render(request,self.template,context=data)
    
    def post(self,request,*args,**kwargs):

       form = self.form_class(request.POST,request.FILES)

       if form.is_valid():
           
           form.save()

           messages.success(request,'movie created successfully')
           
           return redirect('movie-list')
     
       data ={'form':form}

       messages.error(request,'movie creation failed')
       
       return render(request,self.template,context=data)
    
    #Adding with id method
    
# class MovieDetailsView(View):

#     template = 'Movies/Movie-details.html'

#     def get(self,request,*args,**kwargs):

#         id = kwargs.get('id')

#         movie = Movie.objects.get(id=id)

#         data = {'movie':movie,'page':movie.name}

#         return render(request,self.template,context=data)

# Adding with uuid method
    
class MovieDetailsView(View):

    template = 'Movies/Movie-details.html'

    def get(self,request,*args,**kwargs):

        uuid = kwargs.get('uuid')

        movie = Movie.objects.get(uuid=uuid)

        recommended_movies = get_recommended_movies(movie)

        data = {'movie':movie,'page':movie.name,'recommended_movies':recommended_movies}

        return render(request,self.template,context=data)
    
@method_decorator(permitted_user_roles(['Admin']),name='dispatch')
    
class MovieEditView(View):

    form_class = MovieForm

    template = 'movies/movie-edit.html'

    def get(self,request,*args,**kwargs):

        uuid = kwargs.get('uuid')

        movie = Movie.objects.get(uuid=uuid)

        form = self.form_class(instance=movie)

        data = {'form':form,'page':movie.name}

        return render(request,self.template,context=data)
    
    def post(self,request,*args,**kwargs):

        uuid = kwargs.get('uuid')

        movie = Movie.objects.get(uuid=uuid)

        form = self.form_class(request.POST,request.FILES,instance=movie)

        if form.is_valid():

            form.save()

            messages.success(request,' movie updated successfully')

            return redirect('movie-details',uuid=uuid)
        
        data = {'form':form,'page':movie.name}

        return render(request,self.template,context=data)
    
@method_decorator(permitted_user_roles(['Admin']),name='dispatch')
    
class MovieDeleteView(View):

    def get(self,request,*args,**kwargs):

        uuid = kwargs.get('uuid')

        movie = Movie.objects.get(uuid=uuid)

        # movie.delete()

        movie.active_status=False

        movie.save()

        messages.success(request,'movie deleted successfully')

        return redirect('movie-list')
    
@method_decorator(permitted_user_roles(['user']),name='dispatch')
    
class PlayMovie(View):
 
    template = 'movies/movie-play.html'

    def get(self,request,*args,**kwargs):

        user = request.user

        try:
            
            plan = UserSubscription.objects.filter(profile=user,active=True).latest('created_at')
            
        
        except:
            
            pass

        if plan:

            uuid = kwargs.get('uuid')

            movie = Movie.objects.get(uuid=uuid)

            data = {'movie':movie}

            return render(request,self.template,context=data)
        
        else :

            messages.error(request,'you must subscribe a plan before watching')

            return redirect('subscription-list')





    
    