/*
* Copyright (c) 2017 Samsung Electronics Co., Ltd.
*
* Licensed under the Apache License, Version 2.0 (the "License");
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at
*
* http://www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS,
* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
* See the License for the specific language governing permissions and
* limitations under the License.
*
*/

using System;
using System.Runtime.InteropServices;
using Tizen.NUI;
using Tizen.NUI.UIComponents;
using Tizen.NUI.BaseComponents;
using Tizen.NUI.Constants;

namespace HelloWorldAnimationTest
{
    class Example : NUIApplication
    {
        private Animation _animation;
        private TextLabel _text;

        protected override void OnCreate()
        {
            base.OnCreate();
            Initialize();
        }

        public void Initialize()
        {
            Window window = Window.Instance;
            window.BackgroundColor = Color.White;
            window.TouchEvent += OnWindowTouched;

            _text = new TextLabel("Hello NUI World");
            _text.ParentOrigin = ParentOrigin.CenterLeft;
            _text.PivotPoint = PivotPoint.Center;
            _text.HorizontalAlignment = HorizontalAlignment.Center;
            _text.PointSize = 32.0f;
            _text.TextColor = Color.Magenta;
            window.Add(_text);

             _animation = new Animation
            {
                Duration = 2000
            };
            _animation.AnimateTo(_text, "Orientation", new Rotation(new Radian(new Degree(180.0f)), PositionAxis.X), 0, 500, new AlphaFunction(AlphaFunction.BuiltinFunctions.EaseInOutSine));
            _animation.AnimateTo(_text, "Orientation", new Rotation(new Radian(new Degree(0.0f)), PositionAxis.X), 500, 1000, new AlphaFunction(AlphaFunction.BuiltinFunctions.EaseInOutSine));
            _animation.AnimateBy(_text, "ScaleX", 3.0f, 1000, 1500);
            _animation.AnimateBy(_text, "ScaleY", 4.0f, 1500, 2000);

            _animation.EndAction = Animation.EndActions.Discard;
            _animation.Finished += AnimationFinished;
        }

        public void AnimationFinished(object sender, EventArgs e)
        {
            Tizen.Log.Debug("NUI", "AnimationFinished()!");
            if (_animation)
            {
                Tizen.Log.Debug("NUI", "Duration= " + _animation.Duration + "EndAction= " + _animation.EndAction);
            }
        }

        public void OnWindowTouched(object sender, Window.TouchEventArgs e)
        {
            if (e.Touch.GetState(0) == PointStateType.Down)
            {
                 _animation.Play();
            }
        }

        [STAThread]
        static void _Main(string[] args)
        {
            //Tizen.Log.Debug("NUI", "Main() called!");
            Example example = new Example();
            example.Run(args);
        }
    }
}
