[ P11 , P22 ] = meshgrid( 0 : 0.5 : 50 , 0 : 0.5 : 50 );

surf( P22 , P11 , P11 + P22 , 'FaceColor' , 'b' )

hold on

surf( P22 , P11 , P11 .* P22 , 'FaceColor' , 'r' )