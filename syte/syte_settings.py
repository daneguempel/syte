import os

def get_var(var):
	if os.environ.has_key(var):
		return os.environ[var]
	else:
		return ''

DEPLOYMENT_MODE = 'prod'
COMPRESS_REVISION_NUMBER = '1.1'

#Blog Integration: Tumblr
TUMBLR_BLOG_URL = 'daneguempel.tumblr.com'
TUMBLR_API_URL = 'api.tumblr.com/v2/blog/{0}'.format(TUMBLR_BLOG_URL)
TUMBLR_API_KEY = get_var('TUMBLR_API_KEY')

#RSS Feed Integration: (by default use Tumbrl rss feed)
RSS_FEED_ENABLED = True
RSS_FEED_URL = 'http://{0}/rss'.format(TUMBLR_BLOG_URL)

#Twitter Integration
TWITTER_INTEGRATION_ENABLED = True
TWITTER_API_URL = 'http://api.twitter.com/1/statuses/user_timeline.json?include_rts=false&exclude_replies=true&count=50&screen_name='
TWITTER_CONSUMER_KEY = get_var('TWITTER_CONSUMER_KEY')
TWITTER_CONSUMER_SECRET = get_var('TWITTER_CONSUMER_SECRET')
TWITTER_USER_KEY = get_var('TWITTER_USER_KEY')
TWITTER_USER_SECRET = get_var('TWITTER_USER_SECRET')


#Github Integration
GITHUB_INTEGRATION_ENABLED = True
GITHUB_API_URL = 'https://api.github.com/'
GITHUB_ACCESS_TOKEN = get_var('GITHUB_ACCESS_TOKEN')

GITHUB_OAUTH_ENABLED = True
GITHUB_CLIENT_ID = get_var('GITHUB_CLIENT_ID')
GITHUB_CLIENT_SECRET = get_var('GITHUB_CLIENT_SECRET')
GITHUB_OAUTH_AUTHORIZE_URL = get_var('GITHUB_OAUTH_AUTHORIZE_URL')
GITHUB_OAUTH_ACCESS_TOKEN_URL = get_var('GITHUB_OAUTH_ACCESS_TOKEN_URL')


#Dribbble Integration
DRIBBBLE_INTEGRATION_ENABLED = False
DRIBBBLE_API_URL = 'http://api.dribbble.com/players/'


#Instagram Integration
INSTAGRAM_INTEGRATION_ENABLED = True
INSTAGRAM_API_URL = 'https://api.instagram.com/v1/'
INSTAGRAM_ACCESS_TOKEN = get_var('INSTAGRAM_ACCESS_TOKEN')
INSTAGRAM_USER_ID = get_var('INSTAGRAM_USER_ID')

INSTAGRAM_OAUTH_ENABLED = True
INSTAGRAM_CLIENT_ID = get_var('INSTAGRAM_CLIENT_ID')
INSTAGRAM_CLIENT_SECRET = get_var('INSTAGRAM_CLIENT_SECRET')
INSTAGRAM_OAUTH_AUTHORIZE_URL = 'https://api.instagram.com/oauth/authorize'
INSTAGRAM_OAUTH_ACCESS_TOKEN_URL = 'https://api.instagram.com/oauth/access_token'


#Google Analytics
GOOGLE_ANALYTICS_TRACKING_ID = ''


#Disqus Integration
DISQUS_INTEGRATION_ENABLED = False
DISQUS_SHORTNAME = ''


#Lastfm Integration
LASTFM_INTEGRATION_ENABLED = True
LASTFM_API_URL = 'http://ws.audioscrobbler.com/2.0/'
LASTFM_API_KEY = get_var('LASTFM_API_KEY')
LASTFM_USERNAME = get_var('LASTFM_USERNAME')


if DEPLOYMENT_MODE == 'dev':
    SITE_ROOT_URI = 'http://127.0.0.1:8000/'
    DEBUG = True
else:
    DEBUG = False
    SITE_ROOT_URI = 'http://morning-plains-1992.herokuapp.com/'

MEDIA_URL = SITE_ROOT_URI + 'static/'
