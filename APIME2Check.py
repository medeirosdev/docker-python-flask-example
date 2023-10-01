import facebook


def APInstagram(username, token):
    graph = facebook.GraphAPI(access_token=token, version=3.1)
    data = graph.request(
        '17841454088809121?fields=business_discovery.username(' + username + '){followers_count,follows_count,'
                                                                             'media_count,biography,id,'
                                                                             'profile_picture_url,'
                                                                             'username,website,media{comments_count,'
                                                                             'like_count,media_product_type,caption,'
                                                                             'media_type,media_url,'
                                                                             'timestamp}}&access_token=' + str(
            token))

    return data