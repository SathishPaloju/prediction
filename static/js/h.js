/* @rangeColor: #D87469; */
@rangeColor: transparent;
@knobColor: #E96E61;
@knobHoverColor: #DD6B5F;
@knobBorderColor: #fff;
@sliderBackground: #f7f7f7;

body {
  font-family: sans-serif;
  color: #555;
}

.actual {
  text-align: center;
  font-size: x-large;
  margin-top: 40px;
}

#container {
  background-color: @sliderBackground;
  height: 20px;
  top: 50px;
  padding:0;
  position: relative;
  width: 400px;
  margin: 0 auto;
	border-radius: 10px;
  box-shadow: 1px 1px 5px rgba(0,0,0,0.1) inset;

  .knob {
    text-align: center;
    width: 46px;
    height: 46px;
    position: absolute;
    top: -15px;
    z-index: 2;
    border: 2px solid @knobBorderColor;
    border-radius:50%;
    background:  @knobColor;
    box-shadow: 0 0 3px rgba(0, 0, 0, 0.15);
    transition: background-color 0.2s ease-out;


    &:after {
      @borderSize: 1px;
      content: ' ';
      width: 100%;
      height: 100%;
      position: absolute;
      z-index: 10;
      top: -@borderSize; left: -@borderSize;
      text-align: center;
      border-radius: 50%;

      border:  @borderSize solid rgba(0,0,0,0);
    }

    &:hover, &:active {
      background: @knobHoverColor;
    }

    &:active {
      &:after {
        @borderSize: 20px;
        top: -@borderSize; left: -@borderSize;
        border:  @borderSize solid rgba(0,0,0,0.1);
      }
    }
  }
  .range {
    background-color: @rangeColor;
    height: 20px;
    position: relative;
    border-radius: 10px;
  }

  .min-text,
  .max-text,
  .middle-text {
    position: absolute;
    padding-top: 20px;
  }

  .min-text { left: 0; }
  .max-text { right: 0; }
  .middle-text { width: 100%; text-align: center; }
}

