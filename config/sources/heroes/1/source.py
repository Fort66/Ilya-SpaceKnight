from pygame.transform import flip, scale_by
from pygame.image import load


SCALE_VALUE = .225

HERO = {
    'angle': {
        0: {
            'sprite': scale_by(load('images/heroes/1/1.png').convert_alpha(), SCALE_VALUE),
            'weapons': [[], []]
        },
        22: {
            'sprite': scale_by(load('images/heroes/1/1.png').convert_alpha(), SCALE_VALUE),
            'weapons': [[], []]
        },
        45: {
            'sprite': scale_by(load('images/heroes/1/1.png').convert_alpha(), SCALE_VALUE),
            'weapons': [[], []]
        },
        67: {
            'sprite': scale_by(load('images/heroes/1/1.png').convert_alpha(), SCALE_VALUE),
            'weapons': [[], []]
        },
        90: {
            'sprite': scale_by(load('images/heroes/1/1.png').convert_alpha(), SCALE_VALUE),
            'weapons': [[], []]
        },
        112: {
            'sprite': scale_by(load('images/heroes/1/1.png').convert_alpha(), SCALE_VALUE),
            'weapons': [[], []]
        },
        135: {
            'sprite': scale_by(load('images/heroes/1/1.png').convert_alpha(), SCALE_VALUE),
            'weapons': [[], []]
        },
        157: {
            'sprite': scale_by(load('images/heroes/1/1.png').convert_alpha(), SCALE_VALUE),
            'weapons': [[], []]
        },
        180: {
            'sprite': scale_by(load('images/heroes/1/1.png').convert_alpha(), SCALE_VALUE),
            'weapons': [[], []]
        },
        202: {
            'sprite': scale_by(load('images/heroes/1/1.png').convert_alpha(), SCALE_VALUE),
            'weapons': [[], []]
        },
        225: {
            'sprite': scale_by(load('images/heroes/1/1.png').convert_alpha(), SCALE_VALUE),
            'weapons': [[], []]
        },
        247: {
            'sprite': scale_by(load('images/heroes/1/1.png').convert_alpha(), SCALE_VALUE),
            'weapons': [[], []]
        },
        270: {
            'sprite': scale_by(load('images/heroes/1/1.png').convert_alpha(), SCALE_VALUE),
            'weapons': [[], []]
        },
        292: {
            'sprite': scale_by(load('images/heroes/1/1.png').convert_alpha(), SCALE_VALUE),
            'weapons': [[], []]
        },
        315: {
            'sprite': scale_by(load('images/heroes/1/1.png').convert_alpha(), SCALE_VALUE),
            'weapons': [[], []]
        },
        337: {
            'sprite': scale_by(load('images/heroes/1/1.png').convert_alpha(), SCALE_VALUE),
            'weapons': [[], []]
        },
        359: {
            'sprite': scale_by(load('images/heroes/1/1.png').convert_alpha(), SCALE_VALUE),
            'weapons': [[], []]
        },
    }
}