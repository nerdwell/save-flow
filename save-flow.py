#
# save-flow.py
#
# @TheRealNerdwell
#


from mitmproxy import http
import json, time


def response( flow: http.HTTPFlow ) -> None:
    
    if( flow.request.pretty_url.find( '.' ) > -1 ):
        
        s_folder = '/tmp/'
        s_fname = ''
        s_url =''
        s_fname = str( flow.request.timestamp_start )
        if( s_fname.find( '.' ) > -1 ):
            s_fname = s_folder + s_fname[ :(s_fname.find( '.' )) ]
            
        s_url = flow.request.pretty_url.replace( 'https://', '' )
        s_url = s_url.replace( '.', '-' )
        s_url = s_url.replace( '/', '--' )
        s_fname = s_fname + "_" + s_url + ".flow"
        
        try:
            if( len( s_fname ) > 255 ):
                s_fname = s_fname[ :255 ]
            f_out = open( s_fname, 'w+' )
            s_out = ''
            data = { 'request': { 'headers': { } }, 'response': { 'headers': { 'Set-Cookie': [ ] } } }
            
            for header in flow.request.headers:
                if( str( header ).lower() == 'cookie' ):
                    data[ 'request' ][ 'headers' ][ str( header ) ] = { }
                    cookies = str( flow.request.headers[ str( header ) ] ).split( ';' )
                    for cookie in cookies:
                        s_cookie = cookie.split( '=', 1 )
                        if( len( s_cookie ) > 1 ):
                            data[ 'request' ][ 'headers' ][ str( header ) ][ s_cookie[ 0 ].strip() ] = s_cookie[ 1 ].strip()
                        else:
                            data[ 'request' ][ 'headers' ][ str( header ) ][ s_cookie[ 0 ].strip() ] = True
                else:
                    data[ 'request' ][ 'headers' ][ str( header ) ] = str( flow.request.headers[ header ] )
                    
                    
            cnt = 0
            for set_cookie in flow.response.headers.get_all("set-cookie"):
                cnt = cnt + 1
                #print ( 'set-cookie found for # ' + str( cnt ) + ' time.' )
                tmp_set_cookie = { }
                cookies = set_cookie.split( ';' )
                for cookie in cookies:
                    s_cookie = cookie.split( '=', 1 )
                    if( len( s_cookie ) > 1 ):
                        tmp_set_cookie[ s_cookie[ 0 ].strip() ] = s_cookie[ 1 ].strip()
                    else:
                        tmp_set_cookie[ s_cookie[ 0 ].strip() ] = True
                data[ 'response' ][ 'headers' ][ 'Set-Cookie' ].append( tmp_set_cookie )
                    
            for header in flow.response.headers:
                if( str( header ).lower() != 'set-cookie' ):
                    data[ 'response' ][ 'headers' ][ str( header ) ] = str( flow.response.headers[ header ] )
                
                    
            s_out = json.dumps( data )
                
            f_out.write( str( s_out ) )
                        
            f_out.close()
            
            
        except OSError as err:
            print( str( time.mktime( time.gmtime( ) ) ) + ' -- ERR -- problem writing HTTP data to file. error_msg= ' + err.strerror )
            
        except Exception as err:
            print( str( time.mktime( time.gmtime( ) ) ) + ' -- ERR -- problem writing HTTP data to file. exception_type= ' + type( err ).__name__ )
            
        
    
