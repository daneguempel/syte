<<<<<<< HEAD
# -*- coding: utf-8 -*-
=======
import os

>>>>>>> Adding os settings
DEPLOYMENT_MODE = 'prod'
COMPRESS_REVISION_NUMBER = '1.1'

BLOG_PLATFORM = 'tumblr'  # Wordpress or tumblr

#Blog Integration: Tumblr
TUMBLR_BLOG_URL = 'daneguempel.tumblr.com'
TUMBLR_API_URL = 'api.tumblr.com/v2/blog/{0}'.format(TUMBLR_BLOG_URL)
TUMBLR_API_KEY = os.environ['TUMBLR_API_KEY']

#Blog Integration: Wordpress
WORDPRESS_BLOG_URL = '[ENTER WORDPRESS BLOG URL] ex. gordonkoo.wordpress.com'
WORDPRESS_API_URL = 'https://public-api.wordpress.com/rest/v1/sites/{0}'.format(WORDPRESS_BLOG_URL)

#RSS Feed Integration: (by default use Tumblr rss feed)
RSS_FEED_ENABLED = True
RSS_FEED_URL = 'http://{0}/rss'.format(TUMBLR_BLOG_URL)

#Twitter Integration
TWITTER_INTEGRATION_ENABLED = True
TWITTER_API_URL = 'https://api.twitter.com/'
TWITTER_CONSUMER_KEY = os.environ['TWITTER_CONSUMER_KEY']
TWITTER_CONSUMER_SECRET = os.environ['TWITTER_CONSUMER_SECRET']
TWITTER_USER_KEY = os.environ['TWITTER_USER_KEY']
TWITTER_USER_SECRET = os.environ['TWITTER_USER_SECRET']


#Github Integration
GITHUB_INTEGRATION_ENABLED = True
GITHUB_API_URL = 'https://api.github.com/'
GITHUB_ACCESS_TOKEN = os.environ['GITHUB_ACCESS_TOKEN']

GITHUB_OAUTH_ENABLED = True
GITHUB_CLIENT_ID = os.environ['GITHUB_CLIENT_ID']
GITHUB_CLIENT_SECRET = os.environ['GITHUB_CLIENT_SECRET']
GITHUB_OAUTH_AUTHORIZE_URL = os.environ['GITHUB_OAUTH_AUTHORIZE_URL']
GITHUB_OAUTH_ACCESS_TOKEN_URL = os.environ['GITHUB_OAUTH_ACCESS_TOKEN_URL']


#Stack Overflow Integration
STACKOVERFLOW_INTEGRATION_ENABLED = True
STACKOVERFLOW_API_URL = 'http://api.stackoverflow.com/1.1/'


#Dribbble Integration
DRIBBBLE_INTEGRATION_ENABLED = False
DRIBBBLE_API_URL = 'http://api.dribbble.com/players/'


#Instagram Integration
INSTAGRAM_INTEGRATION_ENABLED = True
INSTAGRAM_API_URL = 'https://api.instagram.com/v1/'
INSTAGRAM_ACCESS_TOKEN = os.environ['INSTAGRAM_ACCESS_TOKEN']
INSTAGRAM_USER_ID = os.environ['INSTAGRAM_USER_ID']

INSTAGRAM_OAUTH_ENABLED = True
INSTAGRAM_CLIENT_ID = os.environ['INSTAGRAM_CLIENT_ID']
INSTAGRAM_CLIENT_SECRET = os.environ['INSTAGRAM_CLIENT_SECRET']
INSTAGRAM_OAUTH_AUTHORIZE_URL = 'https://api.instagram.com/oauth/authorize'
INSTAGRAM_OAUTH_ACCESS_TOKEN_URL = 'https://api.instagram.com/oauth/access_token'


#Foursquare Integration
FOURSQUARE_INTEGRATION_ENABLED = True
FOURSQUARE_API_URL = 'https://api.foursquare.com/v2/'
FOURSQUARE_ACCESS_TOKEN = '[ENTER FOURSQUARE ACCESS TOKEN HERE, SEE FOURSQUARE SETUP INSTRUCTIONS]'
FOURSQUARE_SHOW_CURRENT_DAY = True

FOURSQUARE_OAUTH_ENABLED = True
FOURSQUARE_CLIENT_ID = '[ENTER FOURSQUARE CLIENT_ID HERE, SEE FOURSQUARE SETUP INSTRUCTIONS]'
FOURSQUARE_CLIENT_SECRET = '[ENTER FOURSQUARE CLIENT_SECRET HERE, SEE FOURSQUARE SETUP INSTRUCTIONS]'
FOURSQUARE_OAUTH_AUTHORIZE_URL = 'https://foursquare.com/oauth2/authenticate'
FOURSQUARE_OAUTH_ACCESS_TOKEN_URL = 'https://foursquare.com/oauth2/access_token'


#Google Analytics
GOOGLE_ANALYTICS_TRACKING_ID = ''


#ShareThis
SHARETHIS_PUBLISHER_KEY = ''


#Woopra
WOOPRA_TRACKING_DOMAIN = ''
WOOPRA_TRACKING_IDLE_TIMEOUT = 300000  # 5 minutes
WOOPRA_TRACKING_INCLUDE_QUERY = False


#Disqus Integration
DISQUS_INTEGRATION_ENABLED = False
DISQUS_SHORTNAME = ''


#Lastfm Integration
LASTFM_INTEGRATION_ENABLED = True
LASTFM_API_URL = 'http://ws.audioscrobbler.com/2.0/'
<<<<<<< HEAD
LASTFM_API_KEY = '[ENTER LASTFM API_KEY HERE, SEE LASTFM SETUP INSTRUCTIONS]'
=======
LASTFM_API_KEY = os.environ['LASTFM_API_KEY']
LASTFM_USERNAME = os.environ['LASTFM_USERNAME']
>>>>>>> Adding os settings

#SoundCloud Integration
SOUNDCLOUD_INTEGRATION_ENABLED = True
SOUNDCLOUD_API_URL = 'https://api.soundcloud.com/'
SOUNDCLOUD_CLIENT_ID = '[ENTER SOUNDCLOUD APPLICATION CLIENT_ID HERE]'
SOUNDCLOUD_SHOW_ARTWORK = False
SOUNDCLOUD_PLAYER_COLOR = 'ff912b'


#Bitbucket Integration
BITBUCKET_INTEGRATION_ENABLED = True
BITBUCKET_API_URL = 'https://api.bitbucket.org/1.0/'
# Forks count require one connection for each repository,
# set BITBUCKET_SHOW_FORKS to false to disable
BITBUCKET_SHOW_FORKS = False


#Tent.io Integration
TENT_INTEGRATION_ENABLED = True
TENT_ENTITY_URI = '[ENTER YOUR ENTITY URI HERE] ex. https://yourname.tent.is'
TENT_FEED_URL = '[ENTER A URL TO YOUR FEED] ex. https://yourname.tent.is'


#Steam Integration
STEAM_INTEGRATION_ENABLED = True
STEAM_API_URL = 'http://api.steampowered.com/ISteamUser'
STEAM_API_KEY = '[ENTER YOUR STEAM API KEY HERE, SEE STEAM SETUP INSTRUCTIONS]'


#Flickr Integration
FLICKR_INTEGRATION_ENABLED = True
FLICKR_ID = '[ENTER YOUR FLICKR ID (NOT USERNAME) HERE]' # You do your username->ID lookup here: http://idgettr.com/


SITEMAP_ENABLED = False

if DEPLOYMENT_MODE == 'dev':
    SITE_ROOT_URI = 'http://127.0.0.1:8000/'
    DEBUG = True
else:
    DEBUG = False
    SITE_ROOT_URI = 'http://morning-plains-1992.herokuapp.com/'

MEDIA_URL = SITE_ROOT_URI + 'static/'
