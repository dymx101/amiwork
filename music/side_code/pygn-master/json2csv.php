<?php
	$userId = 207;
	$doWhat = 'playlist';
	//$doWhat = 'recommendations';
	
	if($doWhat == 'playlist'){
		$filename = "krishnan_playlistinfo.txt";
		$outfilename = "kg_playlist.csv";
	}
	else{
			$filename = "krishnan_recoinfo.txt";
	$outfilename = "kg_recommendations.csv";

	}
	$json = file_get_contents($filename);
	
	$objects = json_decode($json);
	//die(var_dump($objects[0]));
	
	
	
	$str = "";
	$i=1;
	$outfile = fopen($outfilename,'w');
	foreach($objects as $obj){	
		$mood = get_object_vars($obj->mood)[1];
		$genre = get_object_vars($obj->genre)[1];
		$tempo = get_object_vars($obj->tempo)[1];
		
		
		$mood = get_object_vars($mood);//FIX THIS FOR ME ;_;
		$genre = get_object_vars($genre);
		$tempo = get_object_vars($tempo);
		//25586,65322,Peaceful,Soul\/R&amp;B,43,Parachutes,Coldplay,Trouble
		// /* 
		//Format for playlist
		if($doWhat == 'playlist'){
			$vals = array( 
				$obj->track_gnid,
				$userId,
				$obj->track_title, 
				$obj->album_artist_name, 
				$mood["TEXT"],
				$genre["TEXT"],
				$tempo["TEXT"]
			);
		}
		else{
			$vals = array( 
				$obj->track_gnid,
				$mood["ID"], 
				$mood["TEXT"],
				$genre["TEXT"], 
				$userId,
				$obj->album_title, 
				$obj->album_artist_name, 
				$obj->track_title,
				$tempo["TEXT"]
			);
		}
	//*/
	
		fputcsv($outfile,$vals);
		
	}
	
	
	/*
	{
    "album_art_url": "http://akamai-b.cdn.cddbp.net/cds/2.0/cover/44AC/7E1D/7A64/7E74_medium_front.jpg?cid=13118464", 
    "album_artist_name": "Missquerada", 
    "album_gnid": "237230930-1C2098EFCE10F2F475DCD11505F4C9AF", 
    "album_title": "Far From Love", 
    "album_year": "", 
    "artist_bio_url": "", 
    "artist_era": {}, 
    "artist_image_url": "", 
    "artist_origin": {}, 
    "artist_type": {}, 
    "genre": {
        "1": {
            "ID": "35469", 
            "TEXT": "Pop"
        }, 
        "2": {
            "ID": "35493", 
            "TEXT": "Western Pop"
        }, 
        "3": {
            "ID": "25608", 
            "TEXT": "Pop Vocal"
        }
    }, 
    "mood": {
        "1": {
            "ID": "42960", 
            "TEXT": "Excited"
        }, 
        "2": {
            "ID": "43053", 
            "TEXT": "Euphoric Energy"
        }
    }, 
    "radio_id": "", 
    "review_url": "", 
    "tempo": {
        "1": {
            "ID": "43078", 
            "TEXT": "Fast Tempo"
        }, 
        "2": {
            "ID": "34292", 
            "TEXT": "Fast"
        }, 
        "3": {
            "ID": "34537", 
            "TEXT": "130s"
        }
    }, 
    "track_artist_name": "", 
    "track_gnid": "237230931-4C10227CC5BC1012216E9A546279989F", 
    "track_number": "1", 
    "track_title": "Far From Love", 
    "tracks": [
        {
            "mood": {
                "1": {
                    "ID": "42960", 
                    "TEXT": "Excited"
                }, 
                "2": {
                    "ID": "43053", 
                    "TEXT": "Euphoric Energy"
                }
            }, 
            "tempo": {
                "1": {
                    "ID": "43078", 
                    "TEXT": "Fast Tempo"
                }, 
                "2": {
                    "ID": "34292", 
                    "TEXT": "Fast"
                }, 
                "3": {
                    "ID": "34537", 
                    "TEXT": "130s"
                }
            }, 
            "track_artist_name": "", 
            "track_gnid": "237230931-4C10227CC5BC1012216E9A546279989F", 
            "track_number": "1", 
            "track_title": "Far From Love"
        }
    ], 
    "xid": ""
}
	
	*/
?>