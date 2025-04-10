# Diagrama de Clases Twitter

```mermaid
classDiagram
    class User {
        -int id
        -string username
        -string email
        -string password_hash
        -string display_name
        -string bio
        -datetime created_at
        -datetime updated_at
        +register()
        +login()
        +updateProfile()
        +followUser()
        +unfollowUser()
        +getFollowers()
        +getFollowing()
        +postTweet()
        +getTweets()
    }
    
    class Tweet {
        -int id
        -int user_id
        -string content
        -datetime created_at
        -datetime updated_at
        +create()
        +delete()
        +getLikes()
        +getReplies()
        +getRetweets()
    }
    
    class Retweet {
        -int id
        -int user_id
        -int tweet_id
        -string comment
        -datetime created_at
        +create()
        +delete()
    }
    
    class Reply {
        -int id
        -int user_id
        -int tweet_id
        -int parent_reply_id
        -string content
        -datetime created_at
        +create()
        +delete()
        +getLikes()
    }
    
    class Like {
        -int id
        -int user_id
        -int tweet_id
        -int reply_id
        -datetime created_at
        +create()
        +delete()
    }
    
    class Message {
        -int id
        -int sender_id
        -int recipient_id
        -string content
        -boolean is_read
        -datetime created_at
        +create()
        +markAsRead()
        +delete()
    }
    
    class Hashtag {
        -int id
        -string tag
        -datetime created_at
        +create()
        +getTweets()
        +getTrending()
    }
    
    class TweetHashtag {
        -int tweet_id
        -int hashtag_id
    }
    
    class Preference {
        -int id
        -int user_id
        -boolean dark_mode
        -boolean notification_enabled
        -string language
        -datetime updated_at
        +update()
        +getPreferences()
    }
    
    class Security {
        -int id
        -int user_id
        -boolean two_factor_enabled
        -string recovery_email
        -string phone_number
        -datetime updated_at
        +enableTwoFactor()
        +disableTwoFactor()
        +updateRecoveryOptions()
        +validateLogin()
    }
    
    class Location {
        -int id
        -int tweet_id
        -string place_name
        -float latitude
        -float longitude
        -datetime created_at
        +create()
        +delete()
    }
    
    class Image {
        -int id
        -int tweet_id
        -string url
        -string alt_text
        -datetime created_at
        +upload()
        +delete()
    }
    
    class Follow {
        -int follower_id
        -int following_id
        -datetime created_at
    }
    
    User "1" -- "0..*" Tweet : posts
    User "1" -- "0..*" Retweet : creates
    User "1" -- "0..*" Reply : writes
    User "1" -- "0..*" Like : gives
    User "1" -- "0..*" Message : sends
    User "1" -- "1" Preference : has
    User "1" -- "1" Security : has
    User "1" -- "0..*" Follow : follows
    User "1" -- "0..*" Follow : followed by
    
    Tweet "1" -- "0..*" Reply : has
    Tweet "1" -- "0..*" Like : receives
    Tweet "1" -- "0..*" Retweet : has
    Tweet "1" -- "0..1" Location : tagged with
    Tweet "1" -- "0..*" Image : contains
    Tweet "0..*" -- "0..*" Hashtag : contains
    
    TweetHashtag -- Tweet
    TweetHashtag -- Hashtag
    
    Reply "1" -- "0..*" Reply : has
    Reply "1" -- "0..*" Like : receives
```

## Instrucciones para visualizar en VSC

1. Instala la extensión "Markdown Preview Enhanced" o "Mermaid Preview" en Visual Studio Code
2. Abre este archivo
3. Presiona `Ctrl+K V` (Windows/Linux) o `Cmd+K V` (Mac) para ver la vista previa del diagrama
4. También puedes usar la vista previa nativa de Markdown con `Ctrl+Shift+V` o `Cmd+Shift+V`