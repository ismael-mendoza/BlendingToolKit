from abc import ABC, abstractmethod

import astropy.wcs as WCS
import descwl

import btk.cutout


all_surveys = {
    "LSST": {"bands": ("y", "z", "i", "r", "g", "u"), "pixel_scale": 0.2},
    "DES": {"bands": ("i", "r", "g", "z"), "pixel_scale": 0.263},
    "CFHT": {"bands": ("i", "r"), "pixel_scale": 0.185},
    "HSC": {
        "bands": (
            "y",
            "z",
            "i",
            "r",
            "g",
        ),
        "pixel_scale": 0.17,
    },
}


def make_wcs(
    pixel_scale, shape, center_pix=None, center_sky=None, projection=None, naxis=2
):
    """Creates wcs for an image

    Args:
        pixel_scale (float): pixel size in arcseconds
        shape (tuple): shape of the image
        center_pix (tuple): position of the reference pixel used as the center of the
                            affine transform for the wcs.
        center_sky (list):
        naxis (int):
        projection(str):

    Returns:
        wcs: WCS
    """
    if center_pix is None:
        center_pix = [(s + 1) / 2 for s in shape]
    if center_sky is None:
        center_sky = [0 for _ in range(naxis)]
    if projection is None:
        projection = "TAN"
    w = WCS.WCS(naxis=2)
    w.wcs.ctype = ["RA---" + projection, "DEC--" + projection]
    w.wcs.crpix = center_pix
    w.wcs.cdelt = [pixel_scale for _ in range(naxis)]
    w.wcs.crval = center_sky
    w.array_shape = shape
    return w


class ObsConditions(ABC):
    def __init__(self, stamp_size=24):
        """Class that returns observing conditions for a given survey_name and band.
        If the information provided by this class is combined with the blend_catalogs,
        blend postage stamps can be drawn.

        Args:
            stamp_size (float): In arcseconds.

        """
        self.stamp_size = stamp_size

    def get_wcs(self, pixel_scale, center_pix=None, center_sky=None, projection=None):
        pix_stamp_size = int(self.stamp_size / pixel_scale)
        return make_wcs(
            pixel_scale=pixel_scale,
            center_pix=center_pix,
            center_sky=center_sky,
            projection=projection,
            shape=(pix_stamp_size, pix_stamp_size),
        )

    @abstractmethod
    def __call__(self, survey_name, band):
        """
        Args:
            survey_name: Name of the survey which should be available in descwl
            band: filter name to get observing conditions for.

        Returns:
            A btk.cutout.Cutout object.

        """
        pass


class WLDObsConditions(ObsConditions):
    @abstractmethod
    def get_cutout_params(self, survey_name, band, pixel_scale):
        pass

    def get_cutout(self, survey_name, band, pixel_scale):
        """Returns a btk.cutout.Cutout object."""
        cutout_params = self.get_cutout_params(survey_name, band, pixel_scale)
        wcs = self.get_wcs(pixel_scale)
        return btk.cutout.ObsCutout(
            no_analysis=True,
            survey_name=survey_name,
            filter_band=band,
            wcs=wcs,
            **cutout_params
        )

    def __call__(self, survey_name, band):
        pixel_scale = all_surveys[survey_name]["pixel_scale"]
        cutout = self.get_cutout(survey_name, band, pixel_scale)

        if cutout.pixel_scale != pixel_scale:
            raise ValueError(
                "observing condition pixel scale does not "
                "match input pixel scale: {0} == {1}".format(
                    cutout.pixel_scale, pixel_scale
                )
            )
        if cutout.filter_band != band:
            raise ValueError(
                "observing condition band does not "
                "match input band: {0} == {1}".format(cutout.filter_band, band)
            )

        return cutout


class DefaultObsConditions(WLDObsConditions):
    def __init__(self, stamp_size=24):
        """Returns the default observing conditions from the WLD package
        for a given survey_name and band.
        """
        super().__init__(stamp_size)

    def get_cutout_params(self, survey_name, band, pixel_scale):
        # get default survey params
        pix_stamp_size = int(self.stamp_size / pixel_scale)
        cutout_params = descwl.survey.Survey.get_defaults(
            survey_name=survey_name, filter_band=band
        )
        cutout_params["image_width"] = pix_stamp_size
        cutout_params["image_height"] = pix_stamp_size

        # Information for WCS
        cutout_params["center_sky"] = None
        cutout_params["center_pix"] = None
        cutout_params["projection"] = "TAN"

        return cutout_params