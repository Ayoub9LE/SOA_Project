import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RembouresementComponent } from './rembouresement.component';

describe('RembouresementComponent', () => {
  let component: RembouresementComponent;
  let fixture: ComponentFixture<RembouresementComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [RembouresementComponent]
    });
    fixture = TestBed.createComponent(RembouresementComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
