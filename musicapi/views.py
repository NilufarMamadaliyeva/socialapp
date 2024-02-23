from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from shazamio import Serialize, Shazam, GenreMusic
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import generics
from .models import HitMusicModel
from .serializers import HitMusicSerializer
from rest_framework.decorators import api_view
from pytube import YouTube
from youtube_search import YoutubeSearch
import json
import os


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
    return serialized_tracks[offset : offset + limit]


async def music_uz_api(request):
    if request.method == "GET":
        page = int(request.GET.get("page", 1))
        search_query = request.GET.get("query", "")
        limit = int(
            request.GET.get("limit", 10)
        )  # Default limit is 10, adjust as needed
        offset = (page - 1) * limit
        uz_serialized_tracks = await tracks_uz(offset, limit)
        if search_query:
            uz_serialized_tracks = [
                track
                for track in uz_serialized_tracks
                if search_query.lower() in track.title.lower()
            ]
        serialized_data = [track.__dict__ for track in uz_serialized_tracks]
        return JsonResponse({"uz_serialized_tracks": serialized_data})
    else:
        return JsonResponse({"error": "Only GET method is supported"}, status=405)


async def track_tr(offset=0, limit=100):
    shazam = Shazam()
    top_tracks = await shazam.top_country_tracks("TR", offset + limit)
    serialized_tracks = [Serialize.track(data=track) for track in top_tracks["tracks"]]
    return serialized_tracks[offset : offset + limit]


async def music_tr_api(request):
    if request.method == "GET":
        page = int(request.GET.get("page", 1))
        search_query = request.GET.get("query", "")

        limit = int(
            request.GET.get("limit", 10)
        )  # Default limit is 10, adjust as needed
        offset = (page - 1) * limit
        tr_serialized_tracks = await track_tr(offset, limit)
        if search_query:
            tr_serialized_tracks = [
                track
                for track in tr_serialized_tracks
                if search_query.lower() in track.title.lower()
            ]
        serialized_data = [track.__dict__ for track in tr_serialized_tracks]
        return JsonResponse({"tr_serialized_tracks": serialized_data})
    else:
        return JsonResponse({"error": "Only GET method is supported"}, status=405)


async def track_az(offset=0, limit=100):
    shazam = Shazam()
    top_tracks = await shazam.top_country_tracks("AZ", offset + limit)
    serialized_tracks = [Serialize.track(data=track) for track in top_tracks["tracks"]]
    return serialized_tracks[offset : offset + limit]


async def music_az_api(request):
    if request.method == "GET":
        page = int(request.GET.get("page", 1))
        search_query = request.GET.get("query", "")

        limit = int(
            request.GET.get("limit", 10)
        )  # Default limit is 10, adjust as needed
        offset = (page - 1) * limit
        az_serialized_tracks = await track_az(offset, limit)
        if search_query:
            az_serialized_tracks = [
                track
                for track in az_serialized_tracks
                if search_query.lower() in track.title.lower()
            ]
        serialized_data = [track.__dict__ for track in az_serialized_tracks]
        return JsonResponse({"az_serialized_tracks": serialized_data})
    else:
        return JsonResponse({"error": "Only GET method is supported"}, status=405)


async def track_sa(offset=0, limit=100):
    shazam = Shazam()
    top_tracks = await shazam.top_country_tracks("SA", offset + limit)
    serialized_tracks = [Serialize.track(data=track) for track in top_tracks["tracks"]]
    return serialized_tracks[offset : offset + limit]


async def music_sa_api(request):
    if request.method == "GET":
        page = int(request.GET.get("page", 1))
        search_query = request.GET.get("query", "")

        limit = int(
            request.GET.get("limit", 10)
        )  # Default limit is 10, adjust as needed
        offset = (page - 1) * limit
        sa_serialized_tracks = await track_sa(offset, limit)
        if search_query:
            sa_serialized_tracks = [
                track
                for track in sa_serialized_tracks
                if search_query.lower() in track.title.lower()
            ]
        serialized_data = [track.__dict__ for track in sa_serialized_tracks]
        return JsonResponse({"sa_serialized_tracks": serialized_data})
    else:
        return JsonResponse({"error": "Only GET method is supported"}, status=405)


async def track_kz(offset=0, limit=100):
    shazam = Shazam()
    top_tracks = await shazam.top_country_tracks("KZ", offset + limit)
    serialized_tracks = [Serialize.track(data=track) for track in top_tracks["tracks"]]
    return serialized_tracks[offset : offset + limit]


async def music_kz_api(request):
    if request.method == "GET":
        page = int(request.GET.get("page", 1))
        search_query = request.GET.get("query", "")

        limit = int(
            request.GET.get("limit", 10)
        )  # Default limit is 10, adjust as needed
        offset = (page - 1) * limit
        kz_serialized_tracks = await track_kz(offset, limit)
        if search_query:
            kz_serialized_tracks = [
                track
                for track in kz_serialized_tracks
                if search_query.lower() in track.title.lower()
            ]
        serialized_data = [track.__dict__ for track in kz_serialized_tracks]
        return JsonResponse({"kz_serialized_tracks": serialized_data})
    else:
        return JsonResponse({"error": "Only GET method is supported"}, status=405)


async def track_tj(offset=0, limit=100):
    shazam = Shazam()
    top_tracks = await shazam.top_country_tracks("TJ", offset + limit)
    serialized_tracks = [Serialize.track(data=track) for track in top_tracks["tracks"]]
    return serialized_tracks[offset : offset + limit]


async def music_tj_api(request):
    if request.method == "GET":
        page = int(request.GET.get("page", 1))
        search_query = request.GET.get("query", "")

        limit = int(
            request.GET.get("limit", 10)
        )  # Default limit is 10, adjust as needed
        offset = (page - 1) * limit
        tj_serialized_tracks = await track_tj(offset, limit)
        if search_query:
            tj_serialized_tracks = [
                track
                for track in tj_serialized_tracks
                if search_query.lower() in track.title.lower()
            ]
        serialized_data = [track.__dict__ for track in tj_serialized_tracks]
        return JsonResponse({"tj_serialized_tracks": serialized_data})
    else:
        return JsonResponse({"error": "Only GET method is supported"}, status=405)


async def track_kg(offset=0, limit=100):
    shazam = Shazam()
    top_tracks = await shazam.top_country_tracks("KG", offset + limit)
    serialized_tracks = [Serialize.track(data=track) for track in top_tracks["tracks"]]
    return serialized_tracks[offset : offset + limit]


async def music_kg_api(request):
    if request.method == "GET":
        page = int(request.GET.get("page", 1))
        search_query = request.GET.get("query", "")

        limit = int(
            request.GET.get("limit", 10)
        )  # Default limit is 10, adjust as needed
        offset = (page - 1) * limit
        kg_serialized_tracks = await track_kg(offset, limit)
        if search_query:
            kg_serialized_tracks = [
                track
                for track in kg_serialized_tracks
                if search_query.lower() in track.title.lower()
            ]
        serialized_data = [track.__dict__ for track in kg_serialized_tracks]
        return JsonResponse({"kg_serialized_tracks": serialized_data})
    else:
        return JsonResponse({"error": "Only GET method is supported"}, status=405)


# Janr api
async def top_electronic_tracks(offset=0, limit=100):
    shazam = Shazam()
    top_tracks = await shazam.top_world_genre_tracks(
        genre=GenreMusic.ELECTRONIC, limit=offset + limit
    )
    serialized_tracks = [Serialize.track(data=track) for track in top_tracks["tracks"]]
    return serialized_tracks[offset : offset + limit]


async def music_electronic_api(request):
    if request.method == "GET":
        page = int(request.GET.get("page", 1))
        search_query = request.GET.get("query", "")
        limit = int(
            request.GET.get("limit", 10)
        )  # Default limit is 10, adjust as needed
        offset = (page - 1) * limit
        electronic_serialized_tracks = await top_electronic_tracks(offset, limit)
        if search_query:
            electronic_serialized_tracks = [
                track
                for track in electronic_serialized_tracks
                if search_query.lower() in track.title.lower()
            ]
        serialized_data = [track.__dict__ for track in electronic_serialized_tracks]
        return JsonResponse({"electronic_serialized_tracks": serialized_data})
    else:
        return JsonResponse({"error": "Only GET method is supported"}, status=405)


async def top_rock_api(offset=0,limit=100):
    shazam = Shazam()
    top_tracks = await shazam.top_world_genre_tracks(
        genre=GenreMusic.ROCK, limit=offset + limit
    )
    serialized_tracks = [Serialize.track(data=track) for track in top_tracks["tracks"]]
    return serialized_tracks[offset : offset + limit]


async def music_rock_api(request):
    if request.method == "GET":
        page = int(request.GET.get("page", 1))
        search_query = request.GET.get("query", "")

        limit = int(request.GET.get("limit", 10))  # Default limit is 10, adjust as needed
        offset = (page - 1) * limit
        rock_serialized_tracks = await top_rock_api(offset, limit)
        if search_query:
            rock_serialized_tracks = [track for track in rock_serialized_tracks if search_query.lower() in track.title.lower() ]
        serialized_data = [track.__dict__ for track in rock_serialized_tracks]
        return JsonResponse({"rock_serialized_tracks": serialized_data})
    else:
        return JsonResponse({"error": "Only GET method is supported"}, status=405)


async def top_pop_tracks(offset=0, limit=100):
    shazam = Shazam()
    top_tracks = await shazam.top_world_genre_tracks(
        genre=GenreMusic.POP, limit=offset + limit
    )
    serialized_tracks = [Serialize.track(data=track) for track in top_tracks["tracks"]]
    return serialized_tracks[offset : offset + limit]


async def music_pop_api(request):
    if request.method == "GET":
        page = int(request.GET.get("page", 1))
        search_query = request.GET.get("query", "")

        limit = int(
            request.GET.get("limit", 10)
        )  # Default limit is 10, adjust as needed
        offset = (page - 1) * limit
        pop_serialized_tracks = await top_pop_tracks(offset, limit)
        if search_query:
            pop_serialized_tracks = [
                track
                for track in pop_serialized_tracks
                if search_query.lower() in track.title.lower()
            ]
        serialized_data = [track.__dict__ for track in pop_serialized_tracks]
        return JsonResponse({"pop_serialized_tracks": serialized_data})
    else:
        return JsonResponse({"error": "Only GET method is supported"}, status=405)


async def top_dance_tracks(offset, limit):
    shazam = Shazam()
    top_tracks = await shazam.top_world_genre_tracks(
        genre=GenreMusic.DANCE, limit=offset + limit
    )
    serialized_tracks = [Serialize.track(data=track) for track in top_tracks["tracks"]]
    return serialized_tracks[offset : offset + limit]


async def music_dance_api(request):
    if request.method == "GET":
        page = int(request.GET.get("page", 1))
        search_query = request.GET.get("query", "")

        limit = int(
            request.GET.get("limit", 10)
        )  # Default limit is 10, adjust as needed
        offset = (page - 1) * limit
        dance_serialized_tracks = await top_dance_tracks(offset, limit)
        if search_query:
            dance_serialized_tracks = [
                track
                for track in dance_serialized_tracks
                if search_query.lower() in track.title.lower()
            ]
        serialized_data = [track.__dict__ for track in dance_serialized_tracks]
        return JsonResponse({"dance_serialized_tracks": serialized_data})
    else:
        return JsonResponse({"error": "Only GET method is supported"}, status=405)


async def top_rnb_soul_tracks(offset, limit):
    shazam = Shazam()
    top_tracks = await shazam.top_world_genre_tracks(
        genre=GenreMusic.RNB_SOUL, limit=offset + limit
    )
    serialized_tracks = [Serialize.track(data=track) for track in top_tracks["tracks"]]
    return serialized_tracks[offset : offset + limit]


async def music_rnb_soul_api(request):
    if request.method == "GET":
        page = int(request.GET.get("page", 1))
        search_query = request.GET.get("query", "")

        limit = int(
            request.GET.get("limit", 10)
        )  # Default limit is 10, adjust as needed
        offset = (page - 1) * limit
        rnb_soul_serialized_tracks = await top_rnb_soul_tracks(offset, limit)
        if search_query:
            rnb_soul_serialized_tracks = [
                track
                for track in rnb_soul_serialized_tracks
                if search_query.lower() in track.title.lower()
            ]
        serialized_data = [track.__dict__ for track in rnb_soul_serialized_tracks]
        return JsonResponse({"rnb_soul_serialized_tracks": serialized_data})
    else:
        return JsonResponse({"error": "Only GET method is supported"}, status=405)


async def top_alternative_tracks(offset, limit):
    shazam = Shazam()
    top_tracks = await shazam.top_world_genre_tracks(
        genre=GenreMusic.ALTERNATIVE, limit=offset + limit
    )
    serialized_tracks = [Serialize.track(data=track) for track in top_tracks["tracks"]]
    return serialized_tracks[offset : offset + limit]


async def music_alternative_api(request):
    if request.method == "GET":
        page = int(request.GET.get("page", 1))
        search_query = request.GET.get("query", "")

        limit = int(
            request.GET.get("limit", 10)
        )  # Default limit is 10, adjust as needed
        offset = (page - 1) * limit
        alternative_serialized_tracks = await top_alternative_tracks(offset, limit)
        if search_query:
            alternative_serialized_tracks = [
                track
                for track in alternative_serialized_tracks
                if search_query.lower() in track.title.lower()
            ]
        serialized_data = [track.__dict__ for track in alternative_serialized_tracks]
        return JsonResponse({"alternative_serialized_tracks": serialized_data})
    else:
        return JsonResponse({"error": "Only GET method is supported"}, status=405)


async def top_latin_tracks(offset, limit):
    shazam = Shazam()
    top_tracks = await shazam.top_world_genre_tracks(
        genre=GenreMusic.LATIN, limit=offset + limit
    )
    serialized_tracks = [Serialize.track(data=track) for track in top_tracks["tracks"]]
    return serialized_tracks[offset : offset + limit]


async def music_latin_api(request):
    if request.method == "GET":
        page = int(request.GET.get("page", 1))
        search_query = request.GET.get("query", "")

        limit = int(
            request.GET.get("limit", 10)
        )  # Default limit is 10, adjust as needed
        offset = (page - 1) * limit
        latin_serialized_tracks = await top_latin_tracks(offset, limit)
        if search_query:
            latin_serialized_tracks = [
                track
                for track in latin_serialized_tracks
                if search_query.lower() in track.title.lower()
            ]

        serialized_data = [track.__dict__ for track in latin_serialized_tracks]
        return JsonResponse({"latin_serialized_tracks": serialized_data})
    else:
        return JsonResponse({"error": "Only GET method is supported"}, status=405)


async def top_film_tv_tracks(offset, limit):
    shazam = Shazam()
    top_tracks = await shazam.top_world_genre_tracks(
        genre=GenreMusic.FILM_TV_STAGE, limit=offset + limit
    )
    serialized_tracks = [Serialize.track(data=track) for track in top_tracks["tracks"]]
    return serialized_tracks[offset : offset + limit]


async def music_film_tv_api(request):
    if request.method == "GET":
        page = int(request.GET.get("page", 1))
        search_query = request.GET.get("query", "")

        limit = int(
            request.GET.get("limit", 10)
        )  # Default limit is 10, adjust as needed
        offset = (page - 1) * limit
        film_tv_serialized_tracks = await top_film_tv_tracks(offset, limit)

        # Filter tracks based on search query
        if search_query:
            film_tv_serialized_tracks = [
                track
                for track in film_tv_serialized_tracks
                if search_query.lower() in track.title.lower()
            ]

        serialized_data = [track.__dict__ for track in film_tv_serialized_tracks]
        return JsonResponse({"film_tv_serialized_tracks": serialized_data})
    else:
        return JsonResponse({"error": "Only GET method is supported"}, status=405)


# about Shazam music video
async def get_top_about_track(pk):
    shazam = Shazam()
    about_track_data = await shazam.track_about(track_id=pk)
    serialized = Serialize.track(data=about_track_data)
    return serialized


@csrf_exempt
async def about_track_api(request, pk):
    if request.method == "GET":
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
                        {"title": meta.title, "text": meta.text}
                        for meta in getattr(section, "metadata", [])
                    ],
                }
                for section in top_about_track.sections
                if hasattr(section, "metadata")
            ],
        }

        return JsonResponse(response_data)
    else:
        return JsonResponse({"error": "Only GET method is supported"}, status=405)

# Hit Music API

class HitMusicAPIUpdate(generics.UpdateAPIView):
    queryset = HitMusicModel.objects.all()
    serializer_class = HitMusicSerializer

class HitMusicList(generics.ListCreateAPIView):
    queryset = HitMusicModel.objects.all()
    serializer_class = HitMusicSerializer

class HitMusicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = HitMusicModel.objects.all()
    serializer_class = HitMusicSerializer

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import HitMusicModel

def download_track(request, pk):
    try:
        hit_music = get_object_or_404(HitMusicModel, pk=pk)
        file_path = hit_music.track.path
        with open(file_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='audio/mpeg')
            response['Content-Disposition'] = 'attachment; filename="{}"'.format(hit_music.track_name + '.mp3')
            return response
    except Exception as e:
        return HttpResponse(f"Error: {e}", status=500)

    
# Dowload music view

@api_view(['GET'])
def download_song(request, title, subtitle):
    def get_youtube_links_from_json(json_data):
        data = json.loads(json_data)
        videos = data.get("videos", [])
        youtube_links = []
        for video in videos:
            if not video.get("age_restricted"):
                video_id = video.get("id")
                if video_id:
                    youtube_link = f"https://www.youtube.com/watch?v={video_id}"
                    youtube_links.append(youtube_link)
        return youtube_links

    def rename_file_if_exists(file_path):
        if os.path.exists(file_path):
            base, ext = os.path.splitext(file_path)
            index = 1
            new_file_path = f"{base}({index}){ext}"
            while os.path.exists(new_file_path):
                index += 1
                new_file_path = f"{base}({index}){ext}"
            os.rename(file_path, new_file_path)
            return new_file_path
        else:
            return file_path

    def download_song(youtube_url):
        try:
            yt = YouTube(youtube_url)
            video = yt.streams.filter(only_audio=True).first()
            out_file = video.download(output_path=os.path.join(os.path.expanduser("~"), "Downloads"))
            new_file_path = rename_file_if_exists(out_file)  # Fayl nomini o'zgartirish
            return Response({"message": f"Downloaded: {new_file_path}"}, status=200)
        except Exception as e:
            return Response({"message": f"Error: {e}"}, status=400)

    def search_song(title, subtitle):
        query = f"{title} {subtitle}"
        json_data = YoutubeSearch(query).to_json()
        return json_data

    query = f"{title} {subtitle}"
    json_data = YoutubeSearch(query, max_results=1).to_json()
    youtube_links = get_youtube_links_from_json(json_data)

    for youtube_url in youtube_links:
        return download_song(youtube_url)
