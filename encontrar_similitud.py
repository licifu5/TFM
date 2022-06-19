import metodos
#devuelve un array para cada comparartiva entre imagenes con la siguiente estructura: [ [metodo1, valor1], [metodo2, valor2] ...]
def aplicar_metodos(path_img1, path_img2):
    resultados=[]

    escalaGrises=metodos.escalaGrises(path_img1,path_img2)
    resultados.append(['EscalaGrises',escalaGrises])

    normalizado=metodos.normalizado(path_img1,path_img2)
    resultados.append(['Normalizado',normalizado])

    clahe=metodos.clahe(path_img1,path_img2)
    resultados.append(['CLAHE',clahe])

    gabor=metodos.gabor(path_img1,path_img2)
    resultados.append(['Gabor',gabor])

    hog=metodos.hog(path_img1,path_img2)
    resultados.append(['HOG',hog])

    mse=metodos.mse(path_img1,path_img2)
    resultados.append(['MSE',mse])

    ssim=metodos.ssim(path_img1,path_img2)
    resultados.append(['SSIM',ssim])

    histogramaColor=metodos.histogramaColor(path_img1,path_img2)
    resultados.append(['HistogramaColor',histogramaColor])

    lsh=metodos.lsh(path_img1,path_img2)
    resultados.append(['LSH',lsh])

    sift_sim=metodos.sift_sim(path_img1,path_img2)
    resultados.append(['SIFT',sift_sim])

    lpips_method=metodos.lpips_method(path_img1,path_img2)
    resultados.append(['LPIPS',lpips_method])

    return resultados