from django.http import Http404, JsonResponse
from shazamio import Serialize, Shazam,GenreMusic
from django.views.decorators.csrf import csrf_exempt
import asyncio
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import HitMusicModel
from .serializers import HitMusicSerializer

async def main_uz():
    shazam = Shazam()
    top_tracks = await shazam.top_country_tracks("UZ", 10)
    serialized_tracks = [Serialize.track(data=track) for track in top_tracks["tracks"]]
    return serialized_tracks


async def main_tr():
    shazam = Shazam()
    top_tracks = await shazam.top_country_tracks("TR", 10)
    serialized_tracks = [Serialize.track(data=track) for track in top_tracks["tracks"]]
    return serialized_tracks

async def main_az():
    shazam = Shazam()
    top_tracks = await shazam.top_country_tracks("AZ", 10)
    serialized_tracks = [Serialize.track(data=track) for track in top_tracks["tracks"]]
    return serialized_tracks

async def main_sa():
    shazam = Shazam()
    top_tracks = await shazam.top_country_tracks("SA", 10)
    serialized_tracks = [Serialize.track(data=track) for track in top_tracks["tracks"]]
    return serialized_tracks

async def main_kz():
    shazam = Shazam()
    top_tracks = await shazam.top_country_tracks("KZ", 10)
    serialized_tracks = [Serialize.track(data=track) for track in top_tracks["tracks"]]
    return serialized_tracks

async def main_tj():
    shazam = Shazam()
    top_tracks = await shazam.top_country_tracks("TJ", 10)
    serialized_tracks = [Serialize.track(data=track) for track in top_tracks["tracks"]]
    return serialized_tracks


@csrf_exempt
async def music_api(request):
    if request.method == "GET":
        uz_serialized_tracks = await main_uz()
        tr_serialized_tracks = await main_tr()
        az_serialized_tracks = await main_az()
        sa_serialized_tracks = await main_sa()
        kz_serialized_tracks = await main_kz()
        tj_serialized_tracks = await main_tj()


        uz_serialized_data = [track.__dict__ for track in uz_serialized_tracks]
        tr_serialized_data = [track.__dict__ for track in tr_serialized_tracks]
        az_serialized_data = [track.__dict__ for track in az_serialized_tracks]
        sa_serialized_data = [track.__dict__ for track in sa_serialized_tracks]
        kz_serialized_data = [track.__dict__ for track in kz_serialized_tracks]
        tj_serialized_data = [track.__dict__ for track in tj_serialized_tracks]

        return JsonResponse(
            {
                "uz_serialized_tracks": uz_serialized_data,
                "tr_serialized_tracks": tr_serialized_data,
                "az_serialized_tracks": az_serialized_data,
                "sa_serialized_tracks": sa_serialized_data,
                "kz_serialized_tracks": kz_serialized_data,
                "tj_serialized_tracks": tj_serialized_data,
            }
        )
    else:
        return JsonResponse({"error": "Only GET method is supported"}, status=405)


async def tracks_uz(offset=0, limit=100):
    shazam = Shazam()
    top_tracks = await shazam.top_country_tracks("UZ", offset + limit)
    serialized_tracks = [Serialize.track(data=track) for track in top_tracks["tracks"]]
    return serialized_tracks[offset:offset + limit]

async def music_uz_api(request):
    if request.method == "GET":
        page = int(request.GET.get('page', 1))
        limit = int(request.GET.get('limit', 10))  # Default limit is 10, adjust as needed
        offset = (page - 1) * limit
        uz_serialized_tracks = await tracks_uz(offset, limit)
        serialized_data = [track.__dict__ for track in uz_serialized_tracks]
        return JsonResponse({'uz_serialized_tracks': serialized_data})
    else:
        return JsonResponse({'error': 'Only GET method is supported'}, status=405)

async def track_tr(offset=0, limit=100):
    shazam = Shazam()
    top_tracks = await shazam.top_country_tracks("TR", offset + limit)
    serialized_tracks = [Serialize.track(data=track) for track in top_tracks["tracks"]]
    return serialized_tracks[offset:offset + limit]

async def music_tr_api(request):
    if request.method == "GET":
        page = int(request.GET.get('page', 1))
        limit = int(request.GET.get('limit', 10))  # Default limit is 10, adjust as needed
        offset = (page - 1) * limit
        tr_serialized_tracks = await track_tr(offset, limit)
        serialized_data = [track.__dict__ for track in tr_serialized_tracks]
        return JsonResponse({'tr_serialized_tracks': serialized_data})
    else:
        return JsonResponse({'error': 'Only GET method is supported'}, status=405)
        

async def track_az(offset=0, limit=100):
    shazam = Shazam()
    top_tracks = await shazam.top_country_tracks("AZ", offset + limit)
    serialized_tracks = [Serialize.track(data=track) for track in top_tracks["tracks"]]
    return serialized_tracks[offset:offset + limit]

async def music_az_api(request):
    if request.method == "GET":
        page = int(request.GET.get('page', 1))
        limit = int(request.GET.get('limit', 10))  # Default limit is 10, adjust as needed
        offset = (page - 1) * limit
        az_serialized_tracks = await track_az(offset, limit)
        serialized_data = [track.__dict__ for track in az_serialized_tracks]
        return JsonResponse({'az_serialized_tracks': serialized_data})
    else:
        return JsonResponse({'error': 'Only GET method is supported'}, status=405)
    
async def track_az(offset=0, limit=100):
    shazam = Shazam()
    top_tracks = await shazam.top_country_tracks("SA", offset + limit)
    serialized_tracks = [Serialize.track(data=track) for track in top_tracks["tracks"]]
    return serialized_tracks[offset:offset + limit]

async def music_sa_api(request):
    if request.method == "GET":
        page = int(request.GET.get('page', 1))
        limit = int(request.GET.get('limit', 10))  # Default limit is 10, adjust as needed
        offset = (page - 1) * limit
        sa_serialized_tracks = await track_az(offset, limit)
        serialized_data = [track.__dict__ for track in sa_serialized_tracks]
        return JsonResponse({'sa_serialized_tracks': serialized_data})
    else:
        return JsonResponse({'error': 'Only GET method is supported'}, status=405)
    

async def track_az(offset=0, limit=100):
    shazam = Shazam()
    top_tracks = await shazam.top_country_tracks("KZ", offset + limit)
    serialized_tracks = [Serialize.track(data=track) for track in top_tracks["tracks"]]
    return serialized_tracks[offset:offset + limit]

async def music_kz_api(request):
    if request.method == "GET":
        page = int(request.GET.get('page', 1))
        limit = int(request.GET.get('limit', 10))  # Default limit is 10, adjust as needed
        offset = (page - 1) * limit
        kz_serialized_tracks = await track_az(offset, limit)
        serialized_data = [track.__dict__ for track in kz_serialized_tracks]
        return JsonResponse({'kz_serialized_tracks': serialized_data})
    else:
        return JsonResponse({'error': 'Only GET method is supported'}, status=405)
    
async def track_az(offset=0, limit=100):
    shazam = Shazam()
    top_tracks = await shazam.top_country_tracks("TJ", offset + limit)
    serialized_tracks = [Serialize.track(data=track) for track in top_tracks["tracks"]]
    return serialized_tracks[offset:offset + limit]

async def music_tj_api(request):
    if request.method == "GET":
        page = int(request.GET.get('page', 1))
        limit = int(request.GET.get('limit', 10))  # Default limit is 10, adjust as needed
        offset = (page - 1) * limit
        tj_serialized_tracks = await track_az(offset, limit)
        serialized_data = [track.__dict__ for track in tj_serialized_tracks]
        return JsonResponse({'tj_serialized_tracks': serialized_data})
    else:
        return JsonResponse({'error': 'Only GET method is supported'}, status=405)
    
async def track_kg(offset=0, limit=100):
    shazam = Shazam()
    top_tracks = await shazam.top_country_tracks("KG", offset + limit)
    serialized_tracks = [Serialize.track(data=track) for track in top_tracks["tracks"]]
    return serialized_tracks[offset:offset + limit]

async def music_kg_api(request):
    if request.method == "GET":
        page = int(request.GET.get('page', 1))
        limit = int(request.GET.get('limit', 10))  # Default limit is 10, adjust as needed
        offset = (page - 1) * limit
        kg_serialized_tracks = await track_kg(offset, limit)
        serialized_data = [track.__dict__ for track in kg_serialized_tracks]
        return JsonResponse({'kg_serialized_tracks': serialized_data})
    else:
        return JsonResponse({'error': 'Only GET method is supported'}, status=405)
# Janr api
async def top_electronic_tracks(offset=0, limit=100):
    shazam = Shazam()
    top_tracks = await shazam.top_world_genre_tracks(genre=GenreMusic.ELECTRONIC, limit=offset + limit)
    serialized_tracks = [Serialize.track(data=track) for track in top_tracks["tracks"]]
    return serialized_tracks[offset:offset + limit]

async def music_electronic_api(request):
    if request.method == "GET":
        page = int(request.GET.get('page', 1))
        limit = int(request.GET.get('limit', 10))  # Default limit is 10, adjust as needed
        offset = (page - 1) * limit

        electronic_serialized_tracks = await top_electronic_tracks(offset, limit)
        serialized_data = [track.__dict__ for track in electronic_serialized_tracks]
        return JsonResponse({'electronic_serialized_tracks': serialized_data})
    else:
        return JsonResponse({'error': 'Only GET method is supported'}, status=405)


async def top_rock_api(limit=100, offset=0):
    shazam = Shazam()
    top_tracks = await shazam.top_world_genre_tracks(genre=GenreMusic.ROCK, limit=offset + limit)
    serialized_tracks = [Serialize.track(data=track) for track in top_tracks["tracks"]]
    return serialized_tracks[offset:offset + limit]

async def music_rock_api(request):
    if request.method == "GET":
        page = int(request.GET.get('page', 1))
        limit = int(request.GET.get('limit', 10))  # Default limit is 10, adjust as needed
        offset = (page - 1) * limit
        rock_serialized_tracks = await top_rock_api(offset, limit)
        serialized_data = [track.__dict__ for track in rock_serialized_tracks]
        return JsonResponse({'rock_serialized_tracks': serialized_data})
    else:
        return JsonResponse({'error': 'Only GET method is supported'}, status=405)


async def top_pop_tracks(offset=0,limit=100):
    shazam = Shazam()
    top_tracks = await shazam.top_world_genre_tracks(genre=GenreMusic.POP, limit=offset + limit)
    serialized_tracks = [Serialize.track(data=track) for track in top_tracks["tracks"]]
    return serialized_tracks[offset:offset + limit]

async def music_pop_api(request):
    if request.method == "GET":
        page = int(request.GET.get('page', 1))
        limit = int(request.GET.get('limit', 10))  # Default limit is 10, adjust as needed
        offset = (page - 1) * limit
        pop_serialized_tracks = await top_pop_tracks(offset, limit)
        serialized_data = [track.__dict__ for track in pop_serialized_tracks]
        return JsonResponse({'pop_serialized_tracks': serialized_data})
    else:
        return JsonResponse({'error': 'Only GET method is supported'}, status=405)
    

async def top_dance_tracks(offset, limit):
    shazam = Shazam()
    top_tracks = await shazam.top_world_genre_tracks(genre=GenreMusic.DANCE, limit=offset + limit)
    serialized_tracks = [Serialize.track(data=track) for track in top_tracks["tracks"]]
    return serialized_tracks[offset:offset + limit]

async def music_dance_api(request):
    if request.method == "GET":
        page = int(request.GET.get('page', 1))
        limit = int(request.GET.get('limit', 10))  # Default limit is 10, adjust as needed
        offset = (page - 1) * limit
        dance_serialized_tracks = await top_dance_tracks(offset, limit)
        serialized_data = [track.__dict__ for track in dance_serialized_tracks]
        return JsonResponse({'dance_serialized_tracks': serialized_data})
    else:
        return JsonResponse({'error': 'Only GET method is supported'}, status=405)
    
async def top_rnb_soul_tracks(offset, limit):
    shazam = Shazam()
    top_tracks = await shazam.top_world_genre_tracks(genre=GenreMusic.RNB_SOUL, limit=offset + limit)
    serialized_tracks = [Serialize.track(data=track) for track in top_tracks["tracks"]]
    return serialized_tracks[offset:offset + limit]

async def music_rnb_soul_api(request):
    if request.method == "GET":
        page = int(request.GET.get('page', 1))
        limit = int(request.GET.get('limit', 10))  # Default limit is 10, adjust as needed
        offset = (page - 1) * limit
        rnb_soul_serialized_tracks = await top_rnb_soul_tracks(offset, limit)
        serialized_data = [track.__dict__ for track in rnb_soul_serialized_tracks]
        return JsonResponse({'rnb_soul_serialized_tracks': serialized_data})
    else:
        return JsonResponse({'error': 'Only GET method is supported'}, status=405)
    

async def top_alternative_tracks(offset, limit):
    shazam = Shazam()
    top_tracks = await shazam.top_world_genre_tracks(genre=GenreMusic.ALTERNATIVE, limit=offset + limit)
    serialized_tracks = [Serialize.track(data=track) for track in top_tracks["tracks"]]
    return serialized_tracks[offset:offset + limit]

async def music_alternative_api(request):
    if request.method == "GET":
        page = int(request.GET.get('page', 1))
        limit = int(request.GET.get('limit', 10))  # Default limit is 10, adjust as needed
        offset = (page - 1) * limit
        alternative_serialized_tracks = await top_alternative_tracks(offset, limit)
        serialized_data = [track.__dict__ for track in alternative_serialized_tracks]
        return JsonResponse({'alternative_serialized_tracks': serialized_data})
    else:
        return JsonResponse({'error': 'Only GET method is supported'}, status=405)
    

async def top_latin_tracks(offset, limit):
    shazam = Shazam()
    top_tracks = await shazam.top_world_genre_tracks(genre=GenreMusic.LATIN, limit=offset + limit)
    serialized_tracks = [Serialize.track(data=track) for track in top_tracks["tracks"]]
    return serialized_tracks[offset:offset + limit]

async def music_latin_api(request):
    if request.method == "GET":
        page = int(request.GET.get('page', 1))
        limit = int(request.GET.get('limit', 10))  # Default limit is 10, adjust as needed
        offset = (page - 1) * limit
        latin_serialized_tracks = await top_latin_tracks(offset, limit)
        serialized_data = [track.__dict__ for track in latin_serialized_tracks]
        return JsonResponse({'latin_serialized_tracks': serialized_data})
    else:
        return JsonResponse({'error': 'Only GET method is supported'}, status=405)

async def top_film_tv_tracks(offset,limit):
    shazam = Shazam()
    top_tracks = await shazam.top_world_genre_tracks(genre=GenreMusic.FILM_TV, limit=offset + limit)
    serialized_tracks = [Serialize.track(data=track) for track in top_tracks["tracks"]]
    return serialized_tracks[offset:offset + limit]

async def music_film_tv_api(request):
    if request.method == "GET":
        page = int(request.GET.get('page', 1))
        limit = int(request.GET.get('limit', 10))  # Default limit is 10, adjust as needed
        offset = (page - 1) * limit
        film_tv_serialized_tracks = await top_film_tv_tracks(offset, limit)
        serialized_data = [track.__dict__ for track in film_tv_serialized_tracks]
        return JsonResponse({'film_tv_serialized_tracks': serialized_data})
    else:
        return JsonResponse({'error': 'Only GET method is supported'}, status=405)
    
# about Shazam music video
async def get_top_about_track(pk):
    shazam = Shazam()
    about_track_data = await shazam.track_about(track_id=pk)
    serialized = Serialize.track(data=about_track_data)
    return serialized

@csrf_exempt
async def about_track_api(request, pk):
    if request.method == 'GET':
        top_about_track = await get_top_about_track(pk)
        image_urls = []
        for section in top_about_track.sections:
            if hasattr(section, "meta_pages"):
                for meta_page in section.meta_pages:
                    image_urls.append(meta_page.image)
        response_data = {
            "title": top_about_track.title,
            "subtitle": top_about_track.subtitle,
            "artist_id": top_about_track.artist_id,
            "shazam_url": top_about_track.shazam_url,
            "photo_url": image_urls[-1] if image_urls else None,
            "spotify_uri_query": top_about_track.spotify_uri_query,
            "apple_music_url": top_about_track.apple_music_url,
            "ringtone": top_about_track.ringtone,
            "spotify_url": top_about_track.spotify_url,
            "spotify_uri": top_about_track.spotify_uri,
            "youtube_link": top_about_track.youtube_link,
            "sections": [
                {
                    "type": section.type,
                    "tab_name": section.tab_name,
                    "metadata": [
                        {
                            "title": meta.title,
                            "text": meta.text
                        }
                        for meta in getattr(section, "metadata", []) 
                    ]
                }
                for section in top_about_track.sections
                if hasattr(section, "metadata")
            ]
        }

        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Only GET method is supported'}, status=405)

# about hit music
    
class HitMusicListApi(APIView):
    def get(self, request):
        musics = HitMusicModel.objects.all()
        serializer = HitMusicSerializer(musics, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HitMusicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            music = HitMusicModel.objects.get(pk=pk)
        except HitMusicModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = HitMusicSerializer(music, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            music = HitMusicModel.objects.get(pk=pk)
        except HitMusicModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        music.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class HitMusicDetailApi(APIView):
    def get_object(self, pk):
        try:
            return HitMusicModel.objects.get(pk=pk)
        except HitMusicModel.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        music = self.get_object(pk)
        serializer = HitMusicSerializer(music)
        return Response(serializer.data)
    
        
async def search_tracks(query, limit=10):
    shazam = Shazam()
    tracks = await shazam.search_track(query=query, limit=limit)
    return tracks

async def music_search_api(request):
    if request.method == "GET":
        query = request.GET.get('query', '')  # Get the query parameter from the request
        limit = int(request.GET.get('limit', 10))  # Default limit is 10, adjust as needed
        search_results = await search_tracks(query, limit)
        # Extract relevant information from search results
        serialized_data = [
            {
                "title": track["title"],
                "subtitle": track["subtitle"],
                "shazam_url": track["url"],
                # Add more fields as needed
            } for track in search_results
        ]
        return JsonResponse({'search_results': serialized_data})
    else:
        return JsonResponse({'error': 'Only GET method is supported'}, status=405)