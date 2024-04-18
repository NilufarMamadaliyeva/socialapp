from django.urls import path
from .views import (
    download_song,
    music_api,
    music_uz_api,
    music_tr_api,
    music_az_api,
    music_sa_api,
    music_kz_api,
    music_tj_api,
    music_kg_api,
    # janr
    music_electronic_api,
    music_rock_api,
    music_pop_api,
    music_dance_api,
    music_rnb_soul_api,
    music_alternative_api,
    music_latin_api,
    music_film_tv_api,
    about_track_api,
    # Hit Music
    HitMusicDetail,
    HitMusicList,
    HitMusicAPIUpdate,
    download_track,
)

urlpatterns = [
    path("top/home/", music_api),
    path("tracks/uz/", music_uz_api),
    path("tracks/tr/", music_tr_api),
    path("tracks/az/", music_az_api),
    path("tracks/sa/", music_sa_api),
    path("tracks/kz/", music_kz_api),
    path("tracks/tj/", music_tj_api),
    path("tracks/kg/", music_kg_api),
    # janr   
    path("top/electronic/", music_electronic_api),
    path("top/rock/", music_rock_api),
    path("top/pop/", music_pop_api),
    path("top/dance/", music_dance_api),
    path("top/rnb_soul/", music_rnb_soul_api),
    path("top/alternative/", music_alternative_api),
    path("top/latin/", music_latin_api),
    path("top/film_tv/", music_film_tv_api),
    # about music
    path("tracks/<int:pk>/", about_track_api),
    # hit music
    path("tracks/hit/", HitMusicList.as_view()),
    path("tracks/hit/<int:pk>/", HitMusicDetail.as_view()),
    path("tracks/hit/update/<int:pk>/", HitMusicAPIUpdate.as_view()),
    path('tracks/hit/download/<int:pk>/', download_track),
    # dowload shazam tracks
    path(
        "download-song/<str:title>/<str:subtitle>/", download_song, name="download-song"
    ),
]
